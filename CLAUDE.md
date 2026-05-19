# Project: Claude·Skill 文件生成器

## 运行架构
- 本文件由 DeepSeek 模型读取（Claude Code 做壳，DeepSeek 做脑）
- 全部用中文写，指令直接明确，不写解释性长段落
- 结构化标记（如 [STAGE:1]）需加显式说明，因为 DeepSeek 对此类标记输出不稳定

## 项目定义
HTML 单文件工具，对话式交互，帮用户生成 CLAUDE.md 和 SKILL.md 文件。接入多家 AI API，支持模型版本切换与实时验证。

## Automation Mode
MODE: full-auto
原则：用户描述项目 → 一次生成全部文件 → 用户最终审阅 → 导出。中间不打断。
INTERVENTION_POINTS:
- [ ] 唯一确认点：生成完成后，用户审阅最终产物

## Roadmap

### [1] 生成后自检 — 优先级：高
生成完成后自动检查：
- SKILL.md 触发条件与反触发条件是否矛盾
- CLAUDE.md 约束条件之间是否存在冲突
- 输出问题列表，标注严重程度（高/中/低），"高"红色标注，强制确认后才能导出

### [2] SKILL 触发验证 — 优先级：高
验证生成的 SKILL.md 能否被 Claude Code 正确触发：
- 触发条件太宽→被所有任务触发，太窄→永不触发
- 与系统内置行为重叠→AI 不知道该听哪个
- 生成后自动输出验证清单：触发条件具体性 / 反触发条件 / 重叠检查 / 边界覆盖

### [3] 生成质量反馈 — 优先级：中
用户下载后可选评分（1-5分），积累数据改善同类项目的生成质量。

### [4] 目标模型适配 — 优先级：高
提供"我的 Claude Code 用什么模型"选项，生成 CLAUDE.md 时微调措辞风格：
- Claude：英文指令遵循度高，默认风格即可
- DeepSeek：指令须更直接，减少解释空间
- 通义千问：结构化标记需加强稳定性
- 只影响 CLAUDE.md 写作风格，不影响 SKILL.md（SKILL.md 由 Claude Code 解析，与模型无关）

## Tech Stack
- 运行环境：纯浏览器，单 HTML 文件，无服务器
- AI 接入：Anthropic / OpenAI / DeepSeek / 通义千问 / 智谱GLM / Gemini / Moonshot / 自定义
- 存储：localStorage（API Key、模型验证状态）
- 字体：JetBrains Mono + DM Sans（CDN）

## Architecture
- 无构建工具、无框架依赖，HTML + 原生 JS 单文件
- Provider 配置与业务逻辑分离，新增提供商只需在 PROVIDERS 数组加配置
- 状态集中在 state 对象（S），全局无散落变量
- Gemini 特殊处理：URL 动态构建（key 注入 query string）

## Commands
无构建命令，双击 HTML 文件运行。
开发调试：浏览器 DevTools Console 访问 window.S。

## Code Style
- 函数命名：动词+名词，简短（verifyModel, renderPatch, applyP）
- CSS：全部 CSS Variable 驱动，主题色集中在 :root
- 所有 API 调用必须有 try/catch，错误信息展示在对话中，不用 alert
- 修补卡片渲染与采纳逻辑分离，autoApply() 独立于 UI 操作
