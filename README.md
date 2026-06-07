# 项目罗盘 · Project Compass

<div align="center">

![GitHub Stars](https://img.shields.io/github/stars/tybiefh-beep/project-compass?style=flat-square)
![GitHub Forks](https://img.shields.io/github/forks/tybiefh-beep/project-compass?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)
![HTML](https://img.shields.io/badge/HTML-Pure%20Browser-orange?style=flat-square)

**对混沌的项目想法，让它在 4 个问答中自动校准方向，生成可直接落地的 CLAUDE.md + SKILL.md。**

双击 HTML 就能用 | 零依赖 | 纯浏览器运行 | API Key 只存本地

[🚀 快速开始](#快速开始) · [✨ 功能](#功能) · [📖 详细指南](#生成流程7阶段) · [English](./README_EN.md)

</div>

---

## 🎯 这是什么

一个单文件 HTML 网页工具，叫它**「项目罗盘」**——在想法最混沌的时候，用 4 个关键问题帮你校准方向，然后自动生成 Claude Code 需要的两个核心文件：

- **CLAUDE.md** — 项目操作手册，告诉 AI 你的项目怎么跑、注意什么
- **SKILL.md** — 技能定义文件，让 AI 在特定场景下自动触发专业行为

### 为什么选择它？

| 问题 | 传统方式 | Project Compass |
|------|---------|---------------|
| 如何开始？ | 安装 Node.js、npm 依赖... | 双击 HTML 文件 ✅ |
| API Key 安全吗？ | 上传到服务器 ❌ | 本地存储，不上传 ✅ |
| 支持哪些 AI？ | 通常单一服务 | 8+ 模型供应商 ✅ |
| 学习曲线 | 陡峭 | 对话式引导 ✅ |

---

## 🚀 快速开始

### 方法 1：直接下载（推荐）

1. **下载** `claude-skill 生成器.html` 文件
   ```
   • 点击 Files 标签页
   • 找到 claude-skill 生成器.html
   • 点右键 → Save Link As
   ```

2. **打开** - 双击该文件，浏览器会自动打开

3. **验证** - 填入 API Key，点击「验证」

4. **开始生成** - 点击「＋ 新建项目」

### 方法 2：GitHub Pages（在线版本开发中）

> 敬请期待纯在线版本，无需下载

---

## 💻 使用流程

### 第 1 步：配置 AI 提供商

```
左侧栏 → 选择 AI 提供商 → 输入 API Key → 点击「验证」
```

✅ **支持的模型：**

| 提供商 | 可用模型 |
|--------|----------|
| **Claude** (Anthropic) | Opus 4.7 / Sonnet 4.6 / Haiku 4.5 |
| **GPT** (OpenAI) | GPT-4.1 / GPT-4o / o3-mini |
| **DeepSeek** | deepseek-chat / reasoner / coder |
| **通义千问** | qwen-max / plus / turbo |
| **智谱 GLM** | glm-4-plus / flash |
| **Gemini** (Google) | gemini-2.5-pro / flash |
| **Moonshot** | moonshot-v1 系列 |
| **自定义** | 任何 OpenAI 兼容接口 |

### 第 2-7 步：自动生成

点击「＋ 新建项目」后，系统会依次执行：

| 阶段 | ⏱️ 用时 | 做什么 |
|------|--------|--------|
| 1️⃣ 项目描述 | ~1分钟 | 了解你、你的项目、你的痛点 |
| 2️⃣ 工具架构分析 | ~2分钟 | 梳理工具 → 匹配最佳实践 → 给出架构方案 |
| 3️⃣ 自动化识别 | ~1分钟 | 推荐自动化策略，区分 AI 自主操作 vs 人工介入 |
| 4️⃣ CLAUDE.md 生成 | ~2分钟 | 基于前三阶段生成项目操作手册 |
| 5️⃣ SKILL.md 提取 | ~1分钟 | 识别值得封装的操作，逐个生成技能 |
| 6️⃣ 修补审查 | ~1分钟 | 交叉审查两个文件的一致性 |
| 7️⃣ 文件就绪 | - | 下载导出 |

**总耗时**：约 8-10 分钟，一步到位。

---

## ✨ 功能

### 核心功能

- ✅ **对话式引导** - 4 个关键问题引导你理清思路
- ✅ **自动生成 CLAUDE.md** - 项目操作手册一键生成
- ✅ **自动提取 SKILL.md** - 技能定义文件自动分析
- ✅ **7 阶段工作流** - 从混沌想法到可落地文档

### 高级功能

- 🌙 **日/夜模式** - 根据环境自动切换，偏好自动记忆
- 📎 **文件上传** - 支持 .md / .json / .yaml / .txt 上传，作为上下文输入
- 🔧 **工具自优化** - AI 审查并改进生成器自身的逻辑
- 💾 **会话管理** - 生成历史保存，随时查看或修改

### 隐私与安全

- 🔒 **本地存储** - API Key 存在浏览器 localStorage，永不上传
- 🌐 **直连 API** - 所有请求直接从浏览器发往各厂商 API，不经过中间服务器
- 📵 **零跟踪** - 不收集任何用户数据或使用统计

---

## 📚 使用案例

### 📱 Web 应用开发者

**场景**：开发一个新的 React Dashboard，想让 Claude Code 帮助快速迭代  
**收益**：生成 CLAUDE.md，告诉 AI 项目结构、组件规范、状态管理方式  
**结果**：Claude Code 生成的代码与你的标准完全一致 ✅

### 🐍 Python 工具维护者

**场景**：维护多个 CLI 工具，想自动化部分操作  
**收益**：通过 SKILL.md 定义自动化规则，让 Claude 知道何时触发测试/部署  
**结果**：减少 50% 的手动检查工作 ✅

### 🤖 AI 工作流设计师

**场景**：设计复杂的多步骤 prompt workflow  
**收益**：用项目罗盘梳理 workflow 的关键环节和触发条件  
**结果**：生成标准化的 SKILL.md 文件，可直接在 Claude Code 中使用 ✅

---

## 🏗️ 项目结构

```
project-compass/
├── claude-skill 生成器.html    # 📦 主程序（单文件，即用）
├── skills/                      # 📚 7 个内置 SKILL.md 模板
│   ├── ai-failure-pattern-collector/
│   ├── ai-persistent-memory-system/
│   ├── ai-provider-api-integration/
│   ├── ai-reasoning-process-visualizer/
│   ├── local-standalone-html-app/
│   ├── self-evolving-prompt-system/
│   └── structured-intent-document-generation/
├── generated/                   # 📄 示例输出（供参考）
├── README.md                    # 📖 中文文档
├── README_EN.md                 # 📖 英文文档
└── docs/                        # 📋 详细指南（开发中）
```

---

## ⚙️ 技术细节

### 兼容性

- **浏览器** - Chrome、Firefox、Safari、Edge（推荐最新版本）
- **系统** - Windows、macOS、Linux（任何能打开浏览器的系统）
- **模型** - 支持任何 OpenAI 兼容格式的 API

### 已知限制

- ⚠️ 部分模型不兼容 `[STAGE:N]` 格式标记，工具会自动检测并提示
- 💡 **建议使用**：Claude Opus / GPT-4 系列，生成质量最优

### 获取 API Key

| 提供商 | 申请链接 |
|--------|--------|
| Claude | https://console.anthropic.com |
| OpenAI | https://platform.openai.com/api-keys |
| DeepSeek | https://platform.deepseek.com |
| 通义千问 | https://dashscope.console.aliyun.com |
| 智谱 GLM | https://open.bigmodel.cn |
| Gemini | https://aistudio.google.com |
| Moonshot | https://platform.moonshot.cn |

---

## 🔒 隐私政策

- ✅ **零上传** - API Key 和所有数据都存储在你的浏览器本地
- ✅ **直连 API** - 不存在中间服务器，请求直接发往 AI 提供商
- ✅ **离线可用** - 配置好后，即使断网也能查看历史生成的文件

---

## 📝 常见问题

### Q: 下载的 HTML 文件可以转发给别人用吗？

**A**: 完全可以！这是单文件应用，每个人都可以独立使用，互不影响。

### Q: API Key 会被上传吗？

**A**: 不会。所有 Key 都存在浏览器的 localStorage，只在你的设备上。关闭浏览器也不会丢失。

### Q: 支持离线使用吗？

**A**: 不支持——因为需要调用 AI API。但所有数据处理都在本地，只有 API 调用需要网络。

### Q: 生成的文件能直接用吗？

**A**: 95% 的情况可以直接用。剩余 5% 需要根据你的项目稍微调整。推荐先审查一遍。

### Q: 能改进生成结果吗？

**A**: 可以。工具提供「编辑」功能，你可以随时修改任何生成的内容。

---

## 🎁 内置 SKILL 模板

工具自带 7 个专业级 SKILL.md 模板，涵盖：

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
- 🌍 语言翻译
- 📚 文档改进

---

## 📜 许可证

MIT License - 可自由使用、修改和分发

---

## 💬 联系与反馈

- 📧 Issue 讨论 - [GitHub Issues](https://github.com/tybiefh-beep/project-compass/issues)
- 💭 想法分享 - [GitHub Discussions](https://github.com/tybiefh-beep/project-compass/discussions)

---

<div align="center">

**⭐ 如果觉得有帮助，请给个 Star！**

Made with ❤️ by [tybiefh-beep](https://github.com/tybiefh-beep)

[⬆ 回到顶部](#项目罗盘--project-compass)

</div>
