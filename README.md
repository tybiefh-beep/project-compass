# 项目罗盘 · Project Compass

<div align="center">

![GitHub Stars](https://img.shields.io/github/stars/tybiefh-beep/project-compass?style=flat-square)
![GitHub Forks](https://img.shields.io/github/forks/tybiefh-beep/project-compass?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)
![HTML](https://img.shields.io/badge/HTML-Pure%20Browser-orange?style=flat-square)
![Status](https://img.shields.io/badge/status-Production%20Ready-green?style=flat-square)

**🧭 对混沌的项目想法，让它在 4 个问答中自动校准方向，生成可直接落地的 CLAUDE.md + SKILL.md。**

双击 HTML 就能用 | 零依赖 | 纯浏览器运行 | API Key 只存本地 | 永久免费

[🚀 立即开始](#-快速开始--30-秒上手) · [✨ 功能](#-功能) · [📖 完整指南](#-使用流程) · [English](./README_EN.md) · [Issues](https://github.com/tybiefh-beep/project-compass/issues)

</div>

---

## 🎯 这是什么

一个单文件 HTML 网页工具，叫它**「项目罗盘」**——在想法最混沌的时候，用 4 个关键问题帮你校准方向，然后自动生成 Claude Code 需要的两个核心文件：

- **CLAUDE.md** — 项目操作手册，告诉 AI 你的项目怎么跑、注意什么
- **SKILL.md** — 技能定义文件，让 AI 在特定场景下自动触发专业行为

### 为什么选择它？

| 需求 | 传统工具 | Project Compass |
|------|---------|-----------------|
| 💾 **如何安装？** | 需要 Node.js + npm，折腾 30 分钟 | 双击 HTML，立即可用 ⚡ |
| 🔐 **API Key 安全？** | 上传云端，隐私堪忧 ❌ | 仅本地存储，永不上传 🔒 |
| 🤖 **支持哪些 AI？** | 通常只支持一个厂商 | 8+ 模型供应商，随意切换 🌍 |
| 📚 **难度曲线？** | 需要熟悉工具配置 | 对话式引导，4 个问题搞定 💬 |
| 💰 **价格？** | 通常收费或有限制 | 完全开源免费 🎉 |

---

## 🚀 快速开始 | 30 秒上手

### ⚡ 最快方式：3 步启动

**Step 1: 下载** (10 秒)
```
点击 Files → 找到 项目罗盘.html → 右键 Save Link As
```

**Step 2: 打开** (5 秒)
```
双击下载的 HTML 文件 → 浏览器自动打开
```

**Step 3: 验证 API** (15 秒)
```
左侧栏选 AI 提供商 → 填入 API Key → 点「验证」
✅ 一切就绪，开始使用！
```

### 📚 首次使用指南

| 阶段 | 操作 | 耗时 |
|------|------|------|
| 1️⃣ **配置** | 选择 AI 提供商，验证 API Key | 2 分钟 |
| 2️⃣ **创建项目** | 点「＋ 新建项目」| 1 秒 |
| 3️⃣ **描述项目** | 回答 4 个引导问题 | 5 分钟 |
| 4️⃣ **自动生成** | AI 分析并生成文件（7 阶段）| 8 分钟 |
| 5️⃣ **审查修改** | 查看建议，接受或拒绝 | 3 分钟 |
| 6️⃣ **导出下载** | 下载 CLAUDE.md + SKILL.md | 1 分钟 |

**🎯 总耗时：约 20 分钟，从想法到文件**

### 🔗 一键快速链接

| 需要 | 链接 |
|------|------|
| 📥 **下载本工具** | [项目罗盘.html](https://github.com/tybiefh-beep/project-compass/raw/main/项目罗盘.html) |
| 🔑 **申请 Claude API Key** | https://console.anthropic.com |
| 🔑 **申请 OpenAI API Key** | https://platform.openai.com/api-keys |
| 🔑 **申请 DeepSeek API Key** | https://platform.deepseek.com |
| 💻 **查看示例输出** | [generated/](./generated/) |
| 📖 **完整使用指南** | [向下滚动查看](#-使用流程) |

---

## 💻 使用流程

### 第 1 步：配置 AI 提供商

```
左侧栏 → 选择 AI 提供商 → 输入 API Key → 点击「验证」
```

✅ **支持的模型：**

| 提供商 | 可用模型 | 最佳选择 |
|--------|----------|--------|
| **Claude** (Anthropic) | Opus 4.7 / Sonnet 4.6 / Haiku 4.5 | ⭐⭐⭐ Opus |
| **GPT** (OpenAI) | GPT-4.1 / GPT-4o / o3-mini | ⭐⭐⭐ GPT-4o |
| **DeepSeek** | deepseek-chat / reasoner / coder | ⭐⭐ chat |
| **通义千问** | qwen-max / plus / turbo | ⭐⭐ max |
| **智谱 GLM** | glm-4-plus / flash | ⭐⭐ plus |
| **Gemini** (Google) | gemini-2.5-pro / flash | ⭐⭐ pro |
| **Moonshot** | moonshot-v1 系列 | ⭐⭐ v1-8k |
| **自定义** | 任何 OpenAI 兼容接口 | - |

> 💡 **建议：** 首次使用推荐 Claude Opus，生成质量最优。

### 第 2-7 步：自动生成

点击「＋ 新建项目」后，系统会依次执行：

| 阶段 | ⏱️ 用时 | 做什么 | 输出 |
|------|--------|--------|------|
| 1️⃣ 项目描述 | ~1分钟 | 了解你、你的项目、你的痛点 | 项目概览 |
| 2️⃣ 工具架构分析 | ~2分钟 | 梳理工具 → 匹配最佳实践 → 给出架构方案 | 架构建议 |
| 3️⃣ 自动化识别 | ~1分钟 | 推荐自动化策略，区分 AI 自主操作 vs 人工介入 | 自动化规则 |
| 4️⃣ CLAUDE.md 生成 | ~2分钟 | 基于前三阶段生成项目操作手册 | 📄 CLAUDE.md |
| 5️⃣ SKILL.md 提取 | ~1分钟 | 识别值得封装的操作，逐个生成技能 | 📄 SKILL.md |
| 6️⃣ 修补审查 | ~1分钟 | 交叉审查两个文件的一致性 | 修改建议 |
| 7️⃣ 文件就绪 | - | 下载导出 | ✅ 完成 |

**总耗时**：约 8-10 分钟，一步到位。生成的文件可直接用于 Claude Code。

---

## ✨ 功能

### 核心功能

- ✅ **对话式引导** - 4 个关键问题引导你理清思路
- ✅ **自动生成 CLAUDE.md** - 项目操作手册一键生成
- ✅ **自动提取 SKILL.md** - 技能定义文件自动分析
- ✅ **7 阶段工作流** - 从混沌想法到可落地文档
- ✅ **8+ 模型支持** - 随意切换 AI 提供商

### 高级功能

- 🌙 **日/夜模式** - 根据环境自动切换，偏好自动记忆
- 📎 **文件上传** - 支持 .md / .json / .yaml / .txt 上传，作为上下文输入
- 🔧 **工具自优化** - AI 审查并改进生成器自身的逻辑
- 💾 **会话管理** - 生成历史保存，随时查看或修改
- 📝 **文本编辑** - 生成后可直接编辑，无需重新导出

### 隐私与安全

- 🔒 **本地存储** - API Key 存在浏览器 localStorage，永不上传
- 🌐 **直连 API** - 所有请求直接从浏览器发往各厂商 API，不经过中间服务器
- 📵 **零跟踪** - 不收集任何用户数据或使用统计
- ✅ **完全开源** - 代码透明，可自由审查和修改

---

## 📚 使用案例

### 📱 场景 1: Web 应用开发者

**问题**：开发 React Dashboard，却不知道怎么让 Claude Code 理解项目结构  
**解决**：用项目罗盘生成 CLAUDE.md，描述项目结构、组件规范、状态管理  
**效果**：Claude Code 生成的代码与你的标准完全一致，减少审查改动 ✅

### 🐍 场景 2: Python 工具维护者

**问题**：维护多个 CLI 工具，重复的测试/部署流程让人疲劳  
**解决**：定义 SKILL.md，告诉 Claude 何时自动触发测试、何时需要人工介入  
**效果**：自动化工作流，减少 50% 的手动操作 ✅

### 🤖 场景 3: AI 工作流设计师

**问题**：设计复杂 prompt workflow，很难清晰表达每个步骤的触发条件  
**解决**：用项目罗盘梳理 workflow 的关键环节，生成标准化 SKILL.md  
**效果**：SKILL.md 可直接在 Claude Code 中使用，无需改动 ✅

---

## 🏗️ 项目结构

```
project-compass/
├── 项目罗盘.html              # 📦 主程序（单文件，即用）
├── skills/                       # 📚 7 个内置 SKILL.md 模板
│   ├── ai-failure-pattern-collector/        # AI 故障模式收集器
│   ├── ai-persistent-memory-system/         # AI 持久化记忆系统
│   ├── ai-provider-api-integration/         # AI 供应商 API 集成
│   ├── ai-reasoning-process-visualizer/     # AI 推理过程可视化
│   ├── local-standalone-html-app/           # 本地单文件 HTML 应用
│   ├── self-evolving-prompt-system/         # 自进化 Prompt 系统
│   └── structured-intent-document-generation/ # 结构化意图文档生成
├── generated/                    # 📄 示例输出（参考）
├── README.md                     # 📖 中文文档（当前）
├── README_EN.md                  # 📖 英文文档
└── docs/                         # 📋 详细指南（开发中）
```

---

## ⚙️ 技术细节

### 兼容性

- **浏览器** - Chrome、Firefox、Safari、Edge（推荐最新版本）
- **系统** - Windows、macOS、Linux（任何能打开浏览器的系统）
- **模型** - 支持任何 OpenAI 兼容格式的 API
- **文件大小** - 单文件 < 200KB，无需解压安装

### 已知限制

- ⚠️ 部分模型不兼容 `[STAGE:N]` 格式标记，工具会自动检测并提示
- 💡 **建议使用**：Claude Opus / GPT-4 系列，生成质量最优
- ⚠️ 需要联网调用 AI API（所有数据处理都在本地）

### 快速获取 API Key

| 提供商 | 申请链接 | 免费额度 |
|--------|--------|--------|
| Claude | https://console.anthropic.com | $5 试用 |
| OpenAI | https://platform.openai.com/api-keys | $5 试用 |
| DeepSeek | https://platform.deepseek.com | 免费 |
| 通义千问 | https://dashscope.console.aliyun.com | 免费 |
| 智谱 GLM | https://open.bigmodel.cn | 免费 |
| Gemini | https://aistudio.google.com | 免费 |
| Moonshot | https://platform.moonshot.cn | 免费 |

> 💡 **省钱提示：** DeepSeek、QianWen、GLM 都提供免费额度，可以先用这些。

---

## 🔒 隐私政策

- ✅ **零上传** - API Key 和所有数据都存储在你的浏览器本地
- ✅ **直连 API** - 不存在中间服务器，请求直接发往 AI 提供商
- ✅ **离线就绪** - 配置好后，即使断网也能查看历史生成的文件
- ✅ **完全开源** - 代码公开，无隐藏逻辑

---

## 📝 常见问题

### Q: 下载的 HTML 文件可以转发给别人用吗？

**A**: 完全可以！这是单文件应用，每个人都可以独立使用，互不影响。完全无副作用。

### Q: API Key 会被上传吗？

**A**: 不会。所有 Key 都存在浏览器的 localStorage，只在你的设备上。即使关闭浏览器也不会丢失（除非主动清空缓存）。

### Q: 支持离线使用吗？

**A**: 不支持实时生成（因为需要调用 AI API）。但所有数据处理都在本地，只有 API 调用需要网络。配置完成后可离线查看历史文件。

### Q: 生成的文件能直接用吗？

**A**: 95% 的情况可以直接用。剩余 5% 需要根据你的特定项目稍微调整。推荐先审查一遍，确认符合你的需求。

### Q: 能改进生成结果吗？

**A**: 可以。工具提供「编辑」功能，你可以随时修改任何生成的内容。也可以重新生成一遍，让 AI 重新分析。

### Q: 这个工具和 Claude Code 什么关系？

**A**: 这个工具为 Claude Code 生成「配置文件」(CLAUDE.md 和 SKILL.md)。有了这两个文件，Claude Code 会更理解你的项目，生成的代码质量更高。

### Q: 支持什么 AI 模型？

**A**: 任何支持 OpenAI API 格式的模型都支持，包括 Claude、GPT、DeepSeek、通义千问、智谱 GLM、Gemini、Moonshot 等。可自由切换。

### Q: 生成一次要多少钱？

**A**: 取决于你选择的 AI 模型。通常一次完整生成（7 个阶段）的成本是 $0.10-$1.00 之间。具体看模型定价。

---

## 🎁 内置 SKILL 模板

工具自带 7 个专业级 SKILL.md 模板，可直接使用或参考：

1. **AI 故障模式收集器** - 记录 AI 犯过的错误，避免重复
2. **AI 持久化记忆系统** - 跨会话记忆管理
3. **AI 供应商 API 集成** - 多模型 API 对接规范
4. **AI 推理过程可视化** - COT 链式思维展示
5. **本地单文件 HTML 应用** - 构建独立 HTML 工具的规范
6. **自进化 Prompt 系统** - Prompt 版本管理与优化
7. **结构化意图文档生成** - 自动化文档生成流程

---

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！特别欢迎：

- 🐛 Bug 报告和修复
- ✨ 新 SKILL 模板提案
- 🌍 语言翻译（新增语言支持）
- 📚 文档改进和完善
- 💡 功能建议和改进

---

## 📜 许可证

**MIT License** - 可自由使用、修改和分发

---

## 💬 联系与反馈

- 🐛 **报告 Bug** - [GitHub Issues](https://github.com/tybiefh-beep/project-compass/issues)
- 💭 **分享想法** - [GitHub Discussions](https://github.com/tybiefh-beep/project-compass/discussions)
- ⭐ **给个 Star** - 如果觉得有帮助，请支持一下！

---

## 🌟 相关资源

- 📖 [CLAUDE.md 写法指南](./docs/CLAUDE.md-guide.md)（开发中）
- 📖 [SKILL.md 写法指南](./docs/SKILL.md-guide.md)（开发中）
- 🎥 [使用演示视频](https://github.com/tybiefh-beep/project-compass/discussions)（开发中）
- 📚 [案例精选](./generated/)

---

<div align="center">

## 👇 现在就开始吧！

[**⬇️ 下载 项目罗盘.html**](https://github.com/tybiefh-beep/project-compass/raw/main/项目罗盘.html)

或者查看 [完整源代码](https://github.com/tybiefh-beep/project-compass)

---

**⭐ 如果觉得有帮助，请给个 Star！** ⭐

Made with ❤️ by [tybiefh-beep](https://github.com/tybiefh-beep)

![](https://img.shields.io/badge/Made%20with-❤-red)
![](https://img.shields.io/badge/Love%20Open%20Source-💚-green)

[⬆ 回到顶部](#项目罗盘--project-compass)

</div>
