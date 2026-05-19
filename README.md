# Claude·Skill 文件生成器

**双击 HTML 就能用的 CLAUDE.md + SKILL.md 对话式生成工具。** 零依赖，纯浏览器运行，API Key 只存本地。

## 这是什么

一个单文件 HTML 网页工具，通过 AI 对话理解你的项目，自动生成 Claude Code 需要的两个核心文件：
- **CLAUDE.md** — 项目操作手册，告诉 AI 你的项目怎么跑、注意什么
- **SKILL.md** — 技能定义文件，让 AI 在特定场景下自动触发专业行为

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

1. 下载 `claude-skill 生成器.html`
2. 双击打开（浏览器）
3. 左侧选 AI 提供商，填入 API Key
4. 告诉 AI 你的项目是做什么的
5. 按阶段生成 CLAUDE.md 和 SKILL.md
6. 审查 AI 的修改建议，采纳或拒绝
7. 导出文件

## 项目结构

```
claude-skill-generator/
├── claude-skill 生成器.html   # 主程序（3108 行单文件）
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
