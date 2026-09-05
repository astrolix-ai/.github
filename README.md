<div align="center">

# 🪐 Syzygy (朔望)

**跨平台 · P2P 直连 · 极致强大的剪贴板效率工作台**  
**Cross-Platform · P2P Direct · The Ultimate Clipboard Productivity Workbench**

---

### 🌐 Language Navigation / 语言切换
[**🇨🇳 简体中文**](#-简体中文) &nbsp; | &nbsp; [**🇬🇧 English**](#-english)

---

</div>

<br/>

<a id="chinese"></a>
# 🇨🇳 简体中文

<div align="center">

[![Platform](https://img.shields.io/badge/平台-macOS%20|%20Windows%20|%20Android%20|%20iOS%20|%20Linux-blue?style=flat-square)](#-平台支持)
[![Architecture](https://img.shields.io/badge/架构-Rust%20%7C%20本地优先%20%7C%20P2P-orange?style=flat-square)](https://github.com/YuniqueUnic)
[![Privacy](https://img.shields.io/badge/隐私-数据完全不上云-success?style=flat-square)](#-隐私与安全机制)
[![License](https://img.shields.io/badge/商业模式-Freemium%20%7C%20BYOK-lightgrey?style=flat-square)](#-版本与权益)

[🌐 全球官网](https://www.syzygysync.com/) · [🇨🇳 中文官网](https://cn.syzygysync.com/) · [📖 详细使用文档](https://zq4znidd7hy.feishu.cn/wiki/LhF5wnMlHioR5YkXVy4cl9lynUh?from=from_copylink) · [💬 提交反馈](https://github.com/YuniqueUnic)

</div>

> [!NOTE]
> **什么是「Syzygy」（朔望）？**  
> 该词来自希腊语，指三个天体在引力系统中排成近乎直线的天文奇观（如日月食）。  
> **“当独立的力量（设备）ALIGN 在一起时，创造出大于各部分之和的价值。”**  
> Syzygy 旨在打破电脑、手机间的数据孤岛，让多端设备无缝协同，提供“工作台级别”的内容流转体验。

---

## 🌟 为什么选择 Syzygy？

绝大多数剪贴板工具仍停留在“单机记录”或“依赖中心化云端服务器中转”的阶段。Syzygy 从底层重新定义了剪贴板与数据流转：

- **⚡ P2P 点对点直连**：设备之间直接通讯，不需要任何第三方云服务器存储你的私人剪贴数据。
- **🛡️ 绝对的本地优先（Local-First）**：剪贴板天然包含密码、聊天记录、私密代码，Syzygy 坚持数据不上云，扫描脱敏全部在端侧完成。
- **🎛️ 不止是剪贴板，更是工作台**：自带开发者级别的格式转换器、富文本与复杂文件即时预览、多引擎 OCR 与翻译。

---

## ✨ 核心特性

### 1. 🔄 跨端 P2P 同步（文本 / 图片 / 文件）
- **一处复制，多端秒达**：支持 Windows、macOS、Android 互联，并可直接从移动端系统“分享面板”无缝导入。
- **双重智能传输机制**：
  - **即时同步模式**：文本、轻量截图秒级全量推送。
  - **按需拉取模式**：大文件（>5MB）仅先同步元数据摘要，由你决定是否在目标设备下载，节省带宽与移动流量。

### 2. 🛠️ 深度内容识别与“瑞士军刀”工作台
针对剪贴板内容，提供专属即时处理动作：
- **文本开发辅助**：字符数统计、空白字符去除、**JSON 格式化校验**、**Base64 编解码**。
- **多格式即时渲染**：
  - 代码自动语法高亮。
  - Markdown 语法即时排版渲染。
  - **SVG 代码 / Figma 节点** 直接渲染为可视图像预览。
- **Office / 压缩包免解压预览**：原生支持 `.xlsx`、`.docx`、`.pptx`、`.zip` 等格式的即时快速查看。

### 3. 🪟 极致快捷操作与悬浮固定
- **快捷唤出面板（Quick Panel）**：
  - macOS 默认快捷键 `<kbd>Option</kbd>` + `<kbd>Shift</kbd>` + `<kbd>V</kbd>`，半屏浮现，方向键左右一键即选即贴。
- **独立置顶看板（Popup Mode）**：
  - 可将任意剪贴项独立“钉”在屏幕最前端，支持自由缩放、透明度调节，写代码或对照设计稿时告别反复切屏。
- **即时原地编辑**：内置轻量编辑器，支持行内批量正则替换、大小写一键转换、快速去除重复行。

### 4. 🔍 OCR 识别 & 多引擎翻译（BYOK）
- **离线/在线 OCR**：截图文字秒变可复制结构化文本。
- **自带密钥生态（BYOK）**：翻译接口自由拔插，原生支持配置百度、DeepL、Google、腾讯、有道及主流大模型 AI 翻译服务，成本可控、数据透明。

### 5. 🔏 隐私盾牌与整理分类
- **智能隐私脱敏**：内置敏感内容感知，可针对 Token、密钥、个人信息等开启即时模糊遮罩。
- **标签与星标**：支持手动/AI 智能分类、收藏夹管理、超级快捷置顶（`<kbd>Ctrl</kbd>` + `<kbd>Option</kbd>` + `<kbd>数字键</kbd>`），配备完善的回收站兜底。

---

## 🖥️ 平台支持

| 平台 | 状态 | 架构 / 说明 |
| :--- | :--- | :--- |
| **macOS** | ![Supported](https://img.shields.io/badge/Status-稳定支持-brightgreen?style=flat-square) | Apple Silicon / Intel 原生适配 |
| **Windows** | ![Supported](https://img.shields.io/badge/Status-稳定支持-brightgreen?style=flat-square) | Windows 10 / 11 深度集成 |
| **Android** | ![Supported](https://img.shields.io/badge/Status-稳定支持-brightgreen?style=flat-square) | 支持系统级剪贴板监控与分享面板导入 |
| **iOS** | ![Pending](https://img.shields.io/badge/Status-App%20Store%20审核中-yellow?style=flat-square) | 即将上架，敬请期待 |
| **Linux** | ![Experimental](https://img.shields.io/badge/Status-理论可用-lightgrey?style=flat-square) | 核心技术栈兼容，社区持续测试中 |

---

## 🗺️ 架构路线图（Roadmap）

Syzygy 不仅是一个剪贴板，它的终局是作为个人数字工作空间（Personal AI Workspace）：

- [x] **Phase 1: 核心基础与数据流（Foundation & P2P Data Flow）**
  - [x] 高性能本地存储引擎（Rust Core）
  - [x] 局域网 P2P 直连与大文件分片按需拉取
  - [x] 跨设备文字、图片、格式文件传输
- [ ] **Phase 2: 语音与多模态输入（Voice & Multimodal）** `In Progress`
  - [ ] 语音即时转文字（Voice-to-Text）
  - [ ] 语音直接驱动智能总结、格式整理与改写
- [ ] **Phase 3: 上下文 AI 与知识流转（Context Layer & AI Chat）**
  - [ ] 剪贴板即 AI 上下文：针对最近复制的素材直接提问、对话、生成
  - [ ] 本地个人知识库与记忆层（Memory Engine）
- [ ] **Phase 4: Agent & MCP 生态化**
  - [ ] 接入 Model Context Protocol (MCP)，将剪贴板、历史素材开放为 AI Agent 可调用的工具环境
  - [ ] 自动化流水线（如：多条资料自动一键聚类排版为演示 PPT/分析报告）

---

## 🔒 隐私与安全机制

> **用户的数据永远属于用户自己。**

1. **零中心服务器存储**：剪贴板所有核心数据全生命周期保存在您本机的持久化数据库中。
2. **端对端直连**：设备间配对依靠加密局域网/P2P 通道，不经过任何云端中转服务器落地保存。
3. **模型与 API 自由掌握**：所有扩展 AI 能力均采用 **BYOK（Bring Your Own Key）** 模式，直接调用官方或自定义模型端点，不插手任何中间数据层。

---

## 💎 版本与权益

Syzygy 坚持对绝大多数核心功能保持**完全免费**开放。如果你需要更强大的多端跨设备协同，欢迎选购高级版席位：

| 套餐方案 | 价格 | 适用场景与权益 |
| :--- | :--- | :--- |
| **社区免费版** | **¥0** | 单机完整工作台、智能预览、格式化转换、BYOK 翻译与 OCR |
| **高级版（1 年席位）** | **¥29** / 年 | 开启电脑端高级版 + 2 台移动端之间无缝 P2P 同步 |
| **高级版（2 年席位）** | **¥49** / 两年 | 长期多设备协作性价比优选 |
| **高级版永久（限时）** | **¥244** / 终身 | 终身买断席位，享有后续全部大版本升级与功能优先体验 |

> *注：1 个席位支持 1 台高级版电脑与最多 2 台免费版手机之间的 P2P 同步网络。*

---

## 👨‍💻 开发者与社区

- **开发者**：[YuniqueUnic](https://github.com/YuniqueUnic)
- **个人博客**：[yunique.top](https://www.yunique.top)
- **全套产品资料与使用指引**：[查看飞书知识库](https://zq4znidd7hy.feishu.cn/wiki/LhF5wnMlHioR5YkXVy4cl9lynUh?from=from_copylink)
- **问题与建议**：欢迎提交 [Issues](https://github.com/YuniqueUnic) 反馈。

---

<br/>
<br/>

<a id="english"></a>
# 🇬🇧 English

<div align="center">

[![Platform](https://img.shields.io/badge/Platform-macOS%20|%20Windows%20|%20Android%20|%20iOS%20|%20Linux-blue?style=flat-square)](#-platform-support)
[![Architecture](https://img.shields.io/badge/Core-Rust%20%7C%20Local--First%20%7C%20P2P-orange?style=flat-square)](https://github.com/YuniqueUnic)
[![Privacy](https://img.shields.io/badge/Privacy-Zero%20Cloud%20Data-success?style=flat-square)](#-privacy--security)
[![License](https://img.shields.io/badge/License-Freemium%20%7C%20BYOK-lightgrey?style=flat-square)](#-plans--pricing)

[🌐 Global Website](https://www.syzygysync.com/) · [🇨🇳 Chinese Website](https://cn.syzygysync.com/) · [📖 Documentation](https://zq4znidd7hy.feishu.cn/wiki/LhF5wnMlHioR5YkXVy4cl9lynUh?from=from_copylink) · [💬 Feedback](https://github.com/YuniqueUnic)

</div>

> [!NOTE]
> **What is "Syzygy"?**  
> Originating from Greek, *syzygy* describes an astronomical alignment where three celestial bodies form a near straight line in a gravitational system (e.g., an eclipse).  
> **"When independent forces (devices) ALIGN together, they create value far greater than the sum of their parts."**  
> Syzygy breaks down device silos between desktop and mobile, ensuring natural content continuity through an unprecedented workbench-grade clipboard experience.

---

## 🌟 Why Syzygy?

Most clipboard managers remain either single-device utilities or rely heavily on third-party cloud servers for synchronization. Syzygy redefines data flow from the ground up:

- **⚡ Direct P2P Synchronization**: Direct device-to-device communication without storing any personal clipboard content on central cloud servers.
- **🛡️ Strictly Local-First**: Clipboards naturally contain sensitive data (passwords, tokens, private code). All indexing, parsing, and sanitization are processed locally on your hardware.
- **🎛️ More than a Clipboard, a Full Workbench**: Integrated with developer-grade formatters, live rich-file previews, multi-engine OCR, and BYOK translation.

---

## ✨ Key Features

### 1. 🔄 Cross-Device P2P Sync (Text / Images / Files)
- **Copy Once, Access Anywhere**: Real-time sync across Windows, macOS, and Android. Supports direct import from mobile system share sheets.
- **Dual Transfer Modes**:
  - **Instant Sync Mode**: Delivers text snippets and screenshots within milliseconds.
  - **On-Demand Pull Mode**: For large files (>5MB), only metadata abstracts are synced automatically. You decide whether and when to download the full payload, saving network bandwidth and mobile storage.

### 2. 🛠️ Smart Format Recognition & Power Workbench
Instant, context-aware actions applied directly to clipboard payloads:
- **Developer Utilities**: Character counting, whitespace stripping, **JSON formatting & validation**, **Base64 encoding/decoding**.
- **Live Rendering**:
  - Syntax highlighting for popular programming languages.
  - In-place Markdown rendering.
  - Direct visualization of **SVG code and Figma nodes**.
- **Native Document Previews**: Quick inspection of `.xlsx`, `.docx`, `.pptx`, and `.zip` archives without extraction.

### 3. 🪟 Streamlined Access & Floating Panels
- **Quick Panel**:
  - Summon via `<kbd>Option</kbd>` + `<kbd>Shift</kbd>` + `<kbd>V</kbd>` (macOS default). Half-screen overlay allows seamless arrow-key navigation and instant paste without breaking your workflow.
- **Floating Popup Mode**:
  - Pin any clipboard snippet into an independent floating window. Supports opacity adjustment, zoom, and "Always on Top"—ideal for coding alongside reference specs.
- **In-Place Inline Editor**: Perform regex batch replacement, case conversion, and deduplication directly inside the clipboard entry.

### 4. 🔍 OCR & Multi-Engine Translation (BYOK)
- **Built-in OCR**: Convert text inside images and screenshots into structured, editable text with one click.
- **Bring Your Own Key (BYOK)**: Connect your own credentials for DeepL, Google, Baidu, Tencent, Youdao, or LLM-based translation endpoints for zero markup and full data ownership.

### 5. 🔏 Privacy Shield & Organization
- **Smart Privacy Blur**: Automatically flags and blurs sensitive information (keys, passwords, tokens) with toggleable privacy masks.
- **Tags & Pinning**: Organize items via manual/AI auto-tagging, Favorites, Trash safeguards, and super shortcuts (`<kbd>Ctrl</kbd>` + `<kbd>Option</kbd>` + `<kbd>0-9</kbd>`).

---

## 🖥️ Platform Support

| Platform | Status | Architecture / Details |
| :--- | :--- | :--- |
| **macOS** | ![Supported](https://img.shields.io/badge/Status-Stable-brightgreen?style=flat-square) | Native Apple Silicon & Intel support |
| **Windows** | ![Supported](https://img.shields.io/badge/Status-Stable-brightgreen?style=flat-square) | Deep integration for Windows 10 / 11 |
| **Android** | ![Supported](https://img.shields.io/badge/Status-Stable-brightgreen?style=flat-square) | System clipboard monitor & Share Sheet import |
| **iOS** | ![Pending](https://img.shields.io/badge/Status-In%20App%20Store%20Review-yellow?style=flat-square) | Coming soon to App Store |
| **Linux** | ![Experimental](https://img.shields.io/badge/Status-Experimental-lightgrey?style=flat-square) | Core components compatible; community testing ongoing |

---

## 🗺️ Product Roadmap

Syzygy is evolving from a clipboard tool into a comprehensive **Personal AI Workspace**:

- [x] **Phase 1: Foundation & P2P Data Flow**
  - [x] High-performance Rust Core storage engine
  - [x] Local LAN P2P direct connection & on-demand chunked transmission
  - [x] Cross-device text, media, and archive transfer
- [ ] **Phase 2: Voice & Multimodal Input** `In Progress`
  - [ ] Real-time Voice-to-Text input
  - [ ] Voice-driven summarization, reformatting, and command invocation
- [ ] **Phase 3: Context Layer & AI Chat**
  - [ ] Clipboard as Context: Directly chat with, query, or transform copied materials
  - [ ] Local Personal Knowledge & Long-Term Memory Engine
- [ ] **Phase 4: Agent & MCP Integration**
  - [ ] Model Context Protocol (MCP) server support: expose clipboard history & files as callable Agent tools
  - [ ] Autonomous workflows (e.g., auto-clustering raw research into slide decks or structured reports)

---

## 🔒 Privacy & Security

> **Your data belongs exclusively to you.**

1. **Zero Central Cloud Storage**: Clipboard payloads are stored solely in your local database.
2. **End-to-End Local Direct Sync**: Devices communicate over encrypted peer-to-peer tunnels without routing plain data through external relay servers.
3. **Transparent BYOK Model**: Third-party AI features call your specified providers directly, without intermediate data aggregation.

---

## 💎 Plans & Pricing

Most features in Syzygy are **completely free**. For high-efficiency multi-device sync, we offer seat subscriptions:

| Tier | Price | Highlights |
| :--- | :--- | :--- |
| **Community Free** | **¥0** | Standalone workbench, rich previews, developer tools, BYOK OCR & translation |
| **Premium (1-Year Seat)** | **¥29** / Year | Enables P2P syncing between 1 Desktop Pro seat and up to 2 Mobile Free apps |
| **Premium (2-Year Seat)** | **¥49** / 2 Years | Cost-effective multi-device sync bundle |
| **Lifetime (Limited Time)**| **¥244** / Lifetime | One-time purchase for perpetual updates and early feature access |

> *Note: Each seat supports seamless P2P pairing between 1 Premium desktop client and up to 2 Free mobile clients.*

---

## 👨‍💻 Developer & Community

Built and maintained by an independent full-stack developer. If Syzygy speeds up your daily workflow, consider giving it a star ⭐️!

- **Developer**: [YuniqueUnic](https://github.com/YuniqueUnic)
- **Blog**: [yunique.top](https://www.yunique.top)
- **Knowledge Base**: [Feishu Wiki Documentation](https://zq4znidd7hy.feishu.cn/wiki/LhF5wnMlHioR5YkXVy4cl9lynUh?from=from_copylink)
- **Inquiries & Bugs**: Feel free to open an [Issue](https://github.com/YuniqueUnic) on GitHub.

<div align="center">
  <sub>Built with ❤️ for multi-device creators & developers worldwide.</sub>
</div>
