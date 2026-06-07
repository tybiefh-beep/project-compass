# 项目罗盘 · Project Compass

**对混沌的项目想法,让它在 4 个问答中自动校准方向,生成可直接落地的 CLAUDE.md + SKILL.md。**

双击 HTML 就能用,零依赖、纯浏览器运行,API Key 只存本地。

## 这是什么

一个单文件 HTML 网页工具,叫它「项目罗盘」——在想法最混沌的时候,用 4 个关键问题帮你校准方向,然后自动生成 Claude Code 需要的两个核心文件:
- **CLAUDE.md** — 项目操作手册,告诉 AI 你的项目怎么跑、注意什么
- **SKILL.md** — 技能定义文件,让 AI 在特定场景下自动触发专业行为

## 为什么用它

- 不会写 CLAUDE.md？跟 AI 聊聊你的项目，它帮你写
- 不确定 SKILL.md 的触发条件怎么写？AI 分析你的需求后给出建议
- 市面上其他工具都要装 Node.js，这个是双击 HTML 就能跑

## 支持的 AI 模型

| 提供商 | 可用模型 |
|--------|----------|
| Claude (Anthropic) | Opus 4.7 / Sonnet 4.6 / Haiku 4.5 及旧版 |
| GPT (OpenAI) | gpt-4.1 / gpt-4o / o4-mini / o3-mini 及旧版 |
| DeepSeek | deepseek-chat / reasoner / coder / v4-pro |
| 通义千问 | qwen-max / plus / turbo 等 |
| 智谱 GLM | glm-4-plus / flash 等 |
| Gemini (Google) | gemini-2.5-pro / flash 等 |
| Moonshot | moonshot-v1 系列 |
| 自定义 | 任何 OpenAI 兼容接口 |

## 怎么用

1. 下载 `项目罗盘.html`
2. 双击打开（浏览器）
3. 左侧选 AI 提供商，填入 API Key，点「验证」确认可用
4. 顶部点击「＋ 新建项目」创建项目
5. 描述你的项目，我会依次：分析工具架构 → 推荐自动化策略 → 生成 CLAUDE.md → 提取 SKILL.md
6. 审查修改建议，采纳或拒绝
7. 导出文件

## 生成流程（7 阶段）

| 阶段 | 做什么 |
|------|--------|
| 1. 项目描述 | 了解你、你的项目、你的痛点 |
| 2. 工具架构分析 | 梳理你的工具 → 匹配最佳实践 → 给出架构方案和 Web UI 合并建议 |
| 3. 自动化识别 | 推荐自动化策略，区分 AI 自主操作 vs 人工介入 |
| 4. CLAUDE.md 生成 | 基于前三阶段生成项目操作手册 |
| 5. SKILL.md 提取 | 识别值得封装的操作，逐个生成技能文件 |
| 6. 修补审查 | 交叉审查两个文件的一致性和完整性 |
| 7. 文件就绪 | 下载导出 |

## 功能

- 🌙 日/夜模式切换，偏好自动记忆
- 📎 支持上传文本文件（.md / .json / .yaml 等）提供上下文
- 🔧 工具逻辑自优化（AI 审查并改进生成器自身）

## 项目结构

```
project-compass/
├── 项目罗盘.html   # 主程序（单文件）
├── skills/                     # 7 个内置 SKILL.md 模板
│   ├── ai-failure-pattern-collector/
│   ├── ai-persistent-memory-system/
│   ├── ai-provider-api-integration/
│   ├── ai-reasoning-process-visualizer/
│   ├── local-standalone-html-app/
│   ├── self-evolving-prompt-system/
│   └── structured-intent-document-generation/
├── tools/                      # 辅助脚本（图片 OCR/分析）
└── generated/                  # 示例输出
```

## 隐私

- API Key 存在浏览器 localStorage，不上传任何服务器
- 所有 AI 请求直接从你的浏览器发到各厂商 API
- 不收集任何数据

## 注意事项

- 需要自行申请各 AI 提供商的 API Key
- 部分模型可能不兼容 `[STAGE:N]` 格式标记，工具会验证并提示
- 建议用 Claude 或 GPT 系列模型，生成质量最好
