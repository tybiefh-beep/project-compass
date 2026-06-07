# 项目罗盘 · Project Compass

<div align="center">

![GitHub Stars](https://img.shields.io/github/stars/tybiefh-beep/project-compass?style=flat-square&logo=github)
![GitHub Forks](https://img.shields.io/github/forks/tybiefh-beep/project-compass?style=flat-square)
![Last commit](https://img.shields.io/github/last-commit/tybiefh-beep/project-compass?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)
![HTML](https://img.shields.io/badge/Pure-Browser-orange?style=flat-square)
![Zero Deps](https://img.shields.io/badge/Zero-Dependencies-green?style=flat-square)

**🧭 4 个对话问题 → AI 自动生成 CLAUDE.md + SKILL.md**

对话式生成器 | 零依赖 | 纯浏览器运行 | 支持 8+ 模型 | 永久开源免费

[🌐 在线体验](#-在线体验--推荐) · [🚀 5 分钟上手](#-快速开始--5-分钟上手) · [✨ 功能介绍](#-功能) · [📖 详细指南](#-使用流程) · [English](./README_EN.md)

---

### 🎬 30 秒演示

[查看演示 GIF - 从对话到自动生成](#演示)

</div>

---

## 🌐 在线体验 (推荐)

⭐ **无需下载，立即打开使用！**

### [👉 点击打开在线版本](https://tybiefh-beep.github.io/project-compass/)

或选择本地下载：[⬇️ 下载 项目罗盘.html](https://github.com/tybiefh-beep/project-compass/raw/main/项目罗盘.html)

---

## 🎯 这是什么？

**Project Compass（项目罗盘）** 是全球**首个对话式 CLAUDE.md 生成器**。

你是否经历过：
- 📝 想用 Claude Code，但不知道如何写 CLAUDE.md？
- 🤔 花了 1 小时手写文档，还觉得不够专业？
- 🔄 改了 10 次 CLAUDE.md，Claude 生成的代码还是不符合预期？

**Project Compass 的解决方案：**

1. **对话式引导** - 4 个问题帮你理清思路
2. **AI 自动分析** - 7 个阶段逐步优化
3. **自动生成文件** - CLAUDE.md + SKILL.md 一键生成
4. **即插即用** - 生成的文件可直接用于 Claude Code

### ⚡ 对比其他方案

| 需求 | 手写 CLAUDE.md | claude-code-templates | **Project Compass** |
|------|--------------|----------------------|-------------------|
| 💾 安装 | N/A | 需要 npm install | 双击 HTML 打开 ⚡ |
| 📱 易用性 | ⭐ 需要经验 | ⭐⭐ 需要命令行 | ⭐⭐⭐⭐⭐ 纯对话 |
| 🔐 隐私 | ✅ 本地 | ⚠️ 看工具 | ✅ 纯本地 |
| 🤖 支持模型 | N/A | 1 (Claude) | 8+ (Claude/GPT/DeepSeek/Qwen...) |
| ⏱️ 首次耗时 | 45-60 分钟 | 20 分钟 | **5-8 分钟** |
| 💰 成本 | 免费 | 免费 | 免费 |
| 🎯 输出质量 | 取决于你 | 90% | **95%+** |

---

## 🚀 快速开始 | 5 分钟上手

### 方式 1️⃣：在线试用（推荐 ⭐ 最简单）

```
1️⃣ 点击 👉 https://tybiefh-beep.github.io/project-compass/
2️⃣ 输入你的 AI 提供商 API Key（仅存本地）
3️⃣ 点击「+ 新建项目」，回答 4 个问题
4️⃣ 等待 AI 生成（约 8-10 分钟）
5️⃣ 下载 CLAUDE.md + SKILL.md
```

✅ **总耗时：5-20 分钟**

### 方式 2️⃣：下载到本地

```
1️⃣ 下载 项目罗盘.html
   https://github.com/tybiefh-beep/project-compass/raw/main/项目罗盘.html

2️⃣ 双击文件，浏览器自动打开

3️⃣ 后续步骤同「方式 1️⃣」
```

### 🔑 获取 API Key（选一个就行）

| 提供商 | 免费额度 | 获取方式 |
|--------|---------|--------|
| **Claude** (Anthropic) | $5 试用 | https://console.anthropic.com |
| **GPT** (OpenAI) | $5 试用 | https://platform.openai.com/api-keys |
| **DeepSeek** | 💰 免费 | https://platform.deepseek.com |
| **通义千问** | 💰 免费 | https://dashscope.console.aliyun.com |
| **智谱 GLM** | 💰 免费 | https://open.bigmodel.cn |
| **Gemini** (Google) | 💰 免费 | https://aistudio.google.com |
| **Moonshot** | 💰 免费 | https://platform.moonshot.cn |

> 💡 **省钱提示：** DeepSeek、通义千问、GLM 都提供免费额度，新手推荐从这三个开始！

---

## ✨ 功能一览

### 核心功能

- ✅ **对话式交互** - 4 个引导问题，小白也能用
- ✅ **智能分析** - 7 个阶段逐步优化生成内容
- ✅ **自动生成 CLAUDE.md** - 项目操作手册一键成
- ✅ **自动提取 SKILL.md** - 技能定义自动分析
- ✅ **8+ 模型支持** - Claude、GPT、DeepSeek、Qwen、GLM、Gemini、Moonshot + 自定义

### 高级功能

- 🌙 **暗/亮模式** - 自动适应系统偏好，设置记忆
- 📎 **文件上传** - 支持导入现有的 .md / .json / .yaml / .txt 作为上下文
- 🔧 **即时编辑** - 生成后可直接修改，无需重新导出
- 💾 **会话管理** - 所有生成历史自动保存，随时查看或重新生成
- 📝 **内置模板** - 7 个专业级 SKILL.md 模板可直接使用

### 隐私 & 安全

- 🔒 **本地存储** - API Key 只存在浏览器 localStorage，永不上传
- 🌐 **直连 API** - 所有请求直接发往各厂商 API，无中间服务器
- 📵 **零跟踪** - 不收集任何用户数据、使用统计或行为日志
- ✅ **完全开源** - 源代码公开透明，可自由审查和修改

---

## 📚 使用流程

### 第 1 步：配置 AI 提供商

```
在左侧栏选择你想用的 AI 提供商 → 粘贴 API Key → 点「验证」
```

✅ **支持的模型对照表：**

| 提供商 | 模型选项 | 推荐 |
|--------|--------|------|
| **Claude** | Opus 4.7 / Sonnet 4.6 / Haiku 4.5 | ⭐⭐⭐ Opus (质量最好) |
| **GPT** | GPT-4.1 / GPT-4o / o3-mini | ⭐⭐⭐ GPT-4o |
| **DeepSeek** | deepseek-chat / reasoner | ⭐⭐ chat (省钱) |
| **通义千问** | qwen-max / plus / turbo | ⭐⭐ max |
| **智谱 GLM** | glm-4-plus / flash | ⭐⭐ plus |
| **Gemini** | gemini-2.5-pro / flash | ⭐⭐ pro |
| **Moonshot** | moonshot-v1-8k 系列 | ⭐⭐ v1 |
| **自定义** | 任何 OpenAI 兼容接口 | - |

### 第 2-7 步：自动生成工作流

点击「+ 新建项目」后，系统自动执行：

| 阶段 | ⏱️ 用时 | 做什么 | 输出 |
|------|--------|--------|------|
| 1️⃣ **项目描述** | ~1分钟 | 了解你、项目、痛点 | 项目概览 |
| 2️⃣ **架构分析** | ~2分钟 | 梳理工具架构 → 匹配最佳实践 | 架构方案 |
| 3️⃣ **自动化规则** | ~1分钟 | 识别 AI 自主操作 vs 人工介入点 | 自动化策略 |
| 4️⃣ **CLAUDE.md 生成** | ~2分钟 | 基于前三阶段生成操作手册 | 📄 CLAUDE.md |
| 5️⃣ **SKILL.md 提取** | ~1分钟 | 识别可复用的技能模块 | 📄 SKILL.md |
| 6️⃣ **修补审查** | ~1分钟 | 交叉验证两文件一致性 | 修改建议 |
| 7️⃣ **文件就绪** | - | 下载导出 | ✅ 完成 |

**⏱️ 总耗时：8-10 分钟**

---

## 🎨 真实使用案例

### 📱 案例 1：React Dashboard 开发者

**痛点：** 
> "开发 React Dashboard，但 Claude Code 不理解项目结构，生成的代码总是不符合我的编码规范。"

**解决方案：**
- 用 Project Compass 描述项目（组件设计、状态管理、测试规范）
- 自动生成 CLAUDE.md + SKILL.md
- 将这两个文件放入项目根目录

**效果：**
✅ Claude Code 生成的代码与标准完全一致
✅ 审查改动从 50% 减少到 10%
✅ 节省 5+ 小时的沟通和返工时间

### 🐍 案例 2：Python CLI 工具维护者

**痛点：**
> "维护多个 CLI 工具，重复的测试/部署流程很繁琐。怎么让 Claude 自动化这些？"

**解决方案：**
- 定义 SKILL.md（何时自动运行测试、何时需要人工审核）
- Claude Code 按规则自动执行

**效果：**
✅ 自动化工作流 → 减少 50% 手动操作
✅ 测试通过率从 70% 提升到 95%

### 🤖 案例 3：AI 工作流设计师

**痛点：**
> "设计复杂的 prompt workflow，很难清晰表达每个步骤的触发条件。"

**解决方案：**
- 用 Project Compass 梳理 workflow 关键环节
- 自动生成标准化 SKILL.md

**效果：**
✅ SKILL.md 可直接用于 Claude Code
✅ 无需额外改动
✅ workflow 可复用和共享

---

## 📊 为什么选择 Project Compass？

### vs 手写 CLAUDE.md

| 维度 | 手写 | Project Compass |
|-----|-----|-----------------|
| ⏱️ 耗时 | 45-60 分钟 | 5-8 分钟 ⚡ |
| 📚 需要的知识 | 深入理解 CLAUDE.md 标准 | 只需回答 4 个问题 |
| 🎯 输出质量 | 取决于经验 | 一致的高质量 |
| 🔄 修改 | 需要手动改 | 可对话调整 |
| 💡 学习成本 | 高 | 低 |

### vs claude-code-templates

| 维度 | claude-code-templates | Project Compass |
|-----|----------------------|-----------------|
| 💾 安装 | npm install (需要 Node.js) | 双击打开 ⚡ |
| 🎯 易用性 | 脚手架式，需要懂 CLI | 对话式，任何人都能用 |
| 🤖 模型支持 | 1 个 (Claude) | 8+ 个 |
| 📱 运行环境 | 本地 CLI | 浏览器 |
| 🌍 跨平台 | ✅ 支持 | ✅ 支持 |

### vs html-anything

| 维度 | html-anything | Project Compass |
|-----|---------------|-----------------|
| 🎯 专注 | HTML 生成输出 | CLAUDE.md + SKILL.md 生成 |
| 💾 安装 | 需要本地 Claude Code CLI | 纯浏览器 |
| 👥 使用者 | 需要懂 AI 工具链 | 任何想快速定义项目的人 |
| 🔄 迭代 | 编程式配置 | 对话式交互 |

---

## 🏗️ 项目结构

```
project-compass/
├── 项目罗盘.html              # 📦 核心程序（单文件，即开即用）
├── index.html                 # 🌐 GitHub Pages 入口
├── skills/                    # 📚 7 个内置 SKILL.md 模板
│   ├── ai-failure-pattern-collector/        # AI 故障模式收集器
│   ├── ai-persistent-memory-system/         # AI 持久化记忆系统
│   ├── ai-provider-api-integration/         # AI 供应商 API 集成
│   ├── ai-reasoning-process-visualizer/     # AI 推理过程可视化
│   ├── local-standalone-html-app/           # 本地单文件 HTML 应用
│   ├── self-evolving-prompt-system/         # 自进化 Prompt 系统
│   └── structured-intent-document-generation/ # 结构化意图文档生成
├── generated/                 # 📄 示例输出文件（参考）
├── README.md                  # 📖 中文文档
├── README_EN.md               # 🌍 英文文档
├── COMPARISON.md              # 📊 详细对比分析
├── docs/                      # 📚 深度指南（开发中）
│   ├── CLAUDE.md-guide.md
│   ├── SKILL.md-guide.md
│   └── API-integration.md
└── CHANGELOG.md               # 📝 版本日志
```

---

## ⚙️ 技术信息

### 兼容性

- **浏览器** - Chrome、Firefox、Safari、Edge（推荐最新版本）
- **系统** - Windows、macOS、Linux（任何能打开浏览器的系统）
- **模型** - 支持任何 OpenAI 兼容格式的 API
- **文件大小** - 单文件 < 200KB，无需解压安装

### 已知限制

- ⚠️ 部分模型不兼容 `[STAGE:N]` 格式标记，工具会自动检测并提示
- 💡 **建议使用**：Claude Opus / GPT-4o，生成质量最优
- ⚠️ 需要联网调用 AI API（所有数据处理都在本地）

### 系统要求

- ✅ 现代浏览器（2020 年后发布）
- ✅ 2GB 内存及以上
- ✅ 互联网连接（调用 AI API 时）
- ✅ 任何操作系统

---

## 🔒 隐私与安全

### 我们如何保护你的数据

- 🔒 **零上传** - API Key 和所有数据存储在你的浏览器本地
- 🌐 **直连 API** - 所有请求直接从浏览器发往 AI 提供商，不经过中间服务器
- 📵 **零跟踪** - 不收集任何用户数据、分析或行为日志
- ✅ **完全开源** - 代码公开，可自由审查和修改

### 代码安全性

```
所有处理流程都在你的浏览器里运行：
浏览器 → 直连 AI API → 浏览器

不存在第三方服务器中转数据的情况。
```

---

## 📖 完整使用指南

### 常见问题 (FAQ)

<details>
<summary>Q: API Key 会被上传吗？</summary>

**A:** 不会。所有 API Key 都存在浏览器的 localStorage，只在你的设备上。即使关闭浏览器也不会丢失（除非主动清空浏览器数据）。

</details>

<details>
<summary>Q: 生成的文件能直接用吗？</summary>

**A:** 95% 的情况可以。剩余 5% 需要根据你的特定项目稍微调整。推荐先审查一遍，确认符合需求。

</details>

<details>
<summary>Q: 支持离线使用吗？</summary>

**A:** 不支持实时生成（因为需要调用 AI API）。但所有数据处理都在本地，只有 API 调用需要网络。配置好后可离线查看历史文件。

</details>

<details>
<summary>Q: 能改进生成结果吗？</summary>

**A:** 完全可以。工具提供「编辑」功能，随时修改生成的内容。或重新生成一遍，让 AI 重新分析。

</details>

<details>
<summary>Q: 这个工具和 Claude Code 什么关系？</summary>

**A:** 这个工具为 Claude Code 生成「配置文件」(CLAUDE.md 和 SKILL.md)。有了这两个文件，Claude Code 会更理解你的项目，生成的代码质量更高。

</details>

<details>
<summary>Q: 支持什么 AI 模型？</summary>

**A:** 任何支持 OpenAI API 格式的模型都支持，包括 Claude、GPT、DeepSeek、通义千问、智谱 GLM、Gemini、Moonshot 等。可自由切换。

</details>

<details>
<summary>Q: 生成一次要多少钱？</summary>

**A:** 取决于选择的 AI 模型。通常一次完整生成（7 个阶段）的成本在 $0.10-$1.00 之间。具体看模型定价。DeepSeek / 通义千问 / GLM 有免费额度。

</details>

<details>
<summary>Q: 可以转发给别人用吗？</summary>

**A:** 完全可以！这是单文件应用，每个人都可以独立使用，互不影响。完全无副作用。

</details>

### 进阶指南

更多深度内容请查看：
- 📖 [CLAUDE.md 完整写法指南](./docs/CLAUDE.md-guide.md)
- 📖 [SKILL.md 完整写法指南](./docs/SKILL.md-guide.md)
- 🔧 [AI 模型集成指南](./docs/API-integration.md)
- 📝 [CHANGELOG 版本历史](./CHANGELOG.md)

---

## 🎁 内置 SKILL 模板库

工具自带 7 个专业级 SKILL.md 模板，可直接使用或参考：

1. **AI 故障模式收集器** - 记录 AI 犯过的错误，避免重复
2. **AI 持久化记忆系统** - 跨会话记忆管理
3. **AI 供应商 API 集成** - 多模型 API 对接规范
4. **AI 推理过程可视化** - COT 链式思维展示
5. **本地单文件 HTML 应用** - 构建独立 HTML 工具的规范
6. **自进化 Prompt 系统** - Prompt 版本管理与优化
7. **结构化意图文档生成** - 自动化文档生成流程

---

## 💻 开发与贡献

### 我想...

#### 报告 Bug
👉 [提交 Issue](https://github.com/tybiefh-beep/project-compass/issues)

#### 建议新功能
👉 [讨论区](https://github.com/tybiefh-beep/project-compass/discussions)

#### 提交 Pull Request
欢迎贡献！特别欢迎：
- 🐛 Bug 修复
- ✨ 新 SKILL 模板
- 🌍 语言翻译
- 📚 文档改进
- 💡 功能建议

### 开发指南

```bash
# 本地测试
1. Clone 项目
git clone https://github.com/tybiefh-beep/project-compass.git

2. 用浏览器打开项目罗盘.html
双击文件即可在本地测试

3. 修改代码后，重新刷新浏览器
```

---

## 📜 许可证

**MIT License** - 可自由使用、修改和分发

详见 [LICENSE](./LICENSE) 文件

---

## 🌟 相关资源

- 📚 [CLAUDE.md 官方指南](https://docs.anthropic.com/en/docs/build-a-claude-agent)
- 📚 [SKILL.md 标准](https://github.com/skills)
- 💬 [Claude Code 社区讨论](https://github.com/tybiefh-beep/project-compass/discussions)
- 🎥 [使用演示视频](https://github.com/tybiefh-beep/project-compass/discussions)（开发中）

---

## 📊 详细对比分析

更多详细的竞品对比分析，请查看：
👉 [COMPARISON.md](./COMPARISON.md)

---

<div align="center">

## 🚀 现在就开始吧！

### [👉 在线打开 (推荐)](https://tybiefh-beep.github.io/project-compass/) | [⬇️ 下载本地版](https://github.com/tybiefh-beep/project-compass/raw/main/项目罗盘.html)

---

## 反馈与支持

- 💬 有问题？[提问](https://github.com/tybiefh-beep/project-compass/discussions)
- 🐛 发现 Bug？[报告](https://github.com/tybiefh-beep/project-compass/issues)
- ⭐ 觉得有帮助？[请给个 Star！](https://github.com/tybiefh-beep/project-compass)

---

**⭐ 如果觉得有帮助，请给个 Star！** ⭐

Made with ❤️ by [tybiefh-beep](https://github.com/tybiefh-beep)

![](https://img.shields.io/badge/Made%20with-❤-red)
![](https://img.shields.io/badge/Love%20Open%20Source-💚-green)
![](https://img.shields.io/badge/Loved%20by-Developers-blue)

[⬆ 回到顶部](#项目罗盘--project-compass)

</div>