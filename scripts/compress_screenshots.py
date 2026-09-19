#!/usr/bin/env python3
"""Compress screenshot/raw/*.png into screenshot/ without visible quality loss.

Strategy (lossless-first, quality-preserving):
  1. pngquant --quality: quantizes to a palette ONLY if it can stay above the
     quality floor; otherwise it skips the file (no forced degradation).
  2. If pngquant is unavailable or skips, fall back to Pillow:
     - try libimagequant-style palette quantization is NOT forced either;
     - instead re-encode losslessly with maximum zlib effort + strip metadata
       (PNG optimize=True), which never changes a single pixel.
  3. oxipng (if present) runs as a final lossless pass on every output.

The script never deletes raw/ and never overwrites an output that is already
up to date (mtime-based skip). Exit code 0 on success.

Usage:
  python3 scripts/compress_screenshots.py            # process raw/ -> ./
  python3 scripts/compress_screenshots.py --force    # ignore up-to-date skip
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = REPO_ROOT / "screenshot" / "raw"
OUT_DIR = REPO_ROOT / "screenshot"

# pngquant quality floor: if the image cannot be palette-quantized while
# keeping quality >= min, pngquant exits with status 99 and we keep the
# lossless result instead. This is the "don't hurt quality" guarantee.
PNGQUANT_MIN_QUALITY = 90
PNGQUANT_MAX_QUALITY = 100


def have(tool: str) -> bool:
    return shutil.which(tool) is not None


def lossless_reencode(src: Path, dst: Path) -> int:
    """Re-encode PNG losslessly with maximum compression. Returns size in bytes."""
    from PIL import Image

    img = Image.open(src)
    img.save(dst, format="PNG", optimize=True, compress_level=9)
    return dst.stat().st_size


def try_pngquant(src: Path, dst: Path) -> tuple[bool, int]:
    """Attempt palette quantization with a hard quality floor.

    Returns (quantized, size). quantized=False means pngquant refused
    (quality floor unreachable) or is unavailable — caller should fall back.
    """
    if not have("pngquant"):
        return False, 0
    result = subprocess.run(
        [
            "pngquant",
            f"--quality={PNGQUANT_MIN_QUALITY}-{PNGQUANT_MAX_QUALITY}",
            "--speed", "1",           # slowest search = best palette
            "--strip",                # drop metadata only, pixels unchanged by policy
            "--force",
            "--output", str(dst),
            "--",
            str(src),
        ],
        capture_output=True,
        text=True,
    )
    if result.returncode == 0 and dst.is_file():
        return True, dst.stat().st_size
    # 99 = quality below minimum -> skip (desired behavior); other codes = real errors
    if result.returncode != 99:
        print(f"  pngquant warning ({result.returncode}): {result.stderr.strip()}", file=sys.stderr)
    return False, 0


def final_oxipng(dst: Path) -> None:
    """Extra lossless squeeze if oxipng exists. Never alters pixels."""
    if not have("oxipng"):
        return
    subprocess.run(
        ["oxipng", "-o", "max", "-strip", "safe", "--", str(dst)],
        capture_output=True,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force", action="store_true", help="recompress even if output is newer")
    args = parser.parse_args()

    if not RAW_DIR.is_dir():
        print(f"raw dir missing: {RAW_DIR}", file=sys.stderr)
        return 1
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    pngs = sorted(RAW_DIR.glob("*.png"))
    if not pngs:
        print("no PNG files in raw/")
        return 0

    print(f"tools: pngquant={'yes' if have('pngquant') else 'no'}  oxipng={'yes' if have('oxipng') else 'no'}")
    print(f"processing {len(pngs)} file(s)\n")

    total_raw = total_out = 0
    failures: list[str] = []

    for src in pngs:
        dst = OUT_DIR / src.name
        if not args.force and dst.is_file() and dst.stat().st_mtime >= src.stat().st_mtime:
            print(f"skip (up to date): {src.name}")
            total_raw += src.stat().st_size
            total_out += dst.stat().st_size
            continue

        tmp = dst.with_suffix(".tmp.png")
        quantized, q_size = try_pngquant(src, tmp)

        if quantized:
            lossless_size = None
            chosen = tmp
        else:
            lossless_size = lossless_reencode(src, tmp)
            chosen = tmp

        final_oxipng(chosen)
        final_size = chosen.stat().st_size

        # Never regress: if the "compressed" file is somehow larger than raw,
        # keep a plain lossless copy instead.
        if final_size >= src.stat().st_size:
            shutil.copyfile(src, dst)
            final_size = dst.stat().st_size
            note = "lossless copy (no gain)"
        else:
            tmp.replace(dst)
            saved = 1 - final_size / src.stat().st_size
            method = "pngquant(palette, q>=%d)" % PNGQUANT_MIN_QUALITY if quantized else "lossless re-encode"
            note = f"{method}  {src.stat().st_size/1e6:.2f}MB -> {final_size/1e6:.2f}MB  (-{saved:.0%})"

        if dst.is_file():
            total_raw += src.stat().st_size
            total_out += final_size
            print(f"ok  {src.name:<40} {note}")
        else:
            failures.append(src.name)
            print(f"FAIL {src.name}", file=sys.stderr)

        if tmp.exists():
            tmp.unlink()

    if total_raw:
        print(f"\ntotal: {total_raw/1e6:.2f}MB -> {total_out/1e6:.2f}MB  (-{1 - total_out/total_raw:.0%})")
    if failures:
        print(f"failed: {failures}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
