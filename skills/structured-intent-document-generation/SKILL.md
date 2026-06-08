---
name: structured-intent-document-generation
description: 通过多阶段对话引导用户将项目意图和技能知识结构化为 CLAUDE.md / SKILL.md 文件的生成系统——阶段标记解析、文件提取、修补建议的监督式采纳。Use when user wants to generate CLAUDE.md, generate SKILL.md, project documentation, structured intent capture, multi-stage dialogue to document. Triggers: CLAUDE.md 生成、SKILL.md 生成、项目文档化、结构化意图捕获、多阶段对话、stage 标记、补丁采纳。
license: MIT
metadata:
  author: 迷途绿意
  version: "3.1"
---

# structured-intent-document-generation

## 触发条件

需要通过对话引导用户将项目意图和技能知识结构化输出为 CLAUDE.md 或 SKILL.md 文件时使用。包括多阶段对话流程设计、stage 标记解析、文件内容从 AI 回复中提取、修补建议的监督式采纳流程。

## 反触发(不适用)

- 用户直接提供完整文档无需生成时
- 纯问答场景不涉及文件输出时
- 文档结构与现有模板差异过大时(强行套模板会丢失信息)
- 一次性短任务不值得结构化时

## Gotchas(易错点)

- **部分模型不输出 `[STAGE:N]` 标记** → 不要强依赖 stage 标记做 UI 联动,fallback 用自然语言"接下来分析.../现在生成.../最后总结..."识别
- **多阶段 AI 容易跑题** → 每个 stage 的 prompt 必须明确"只做本阶段,不要提前做后面的"
- **PATCH JSON 单行解析很脆弱** → 跨行 JSON / 含注释 / 含转义字符都会炸;先尝试 `JSON.parse`,失败再用正则容错
- **修补建议要"可解释"** → 不能只说"建议改 X",要说"因为 Y,所以改 X"
- **采纳/拒绝/修改 三态**别让用户写完整文件 → 提供 diff,让用户只改"接受/拒绝/编辑"几个按钮
- **7 阶段总时长**用户没耐心等 → 合并相似阶段(如 1+2,4+5),控制在 4-5 阶段
- **生成完必须自检** → 触发条件/反触发/覆盖操作是否自洽,矛盾项高亮强制确认
- **文件输出别让 AI 自己造路径** → 路径由前端固定,AI 只输出内容,避免路径注入

## 覆盖操作(必须支持)

- [ ] SYSTEM_PROMPT 设计(7 阶段,每阶段目标 + 输出格式)
- [ ] `[STAGE:N]` 解析与 UI 联动(进度条 + 当前阶段高亮)
- [ ] 正则提取 markdown / xml 代码块(从 AI 回复中抓文件内容)
- [ ] PATCH JSON 单行解析 + 容错
- [ ] patch 采纳/拒绝/修改的三态 UI 与内容回写
- [ ] 生成后自检(触发/反触发/覆盖操作矛盾检测)
- [ ] 阶段跳过(用户说"快进"可跳到下一关键阶段)
- [ ] 多文件并行生成(CLAUDE.md + 多个 SKILL.md 同时输出)

## 工作流(分阶段)

### 1. 立项
- 决定目标文档(CLAUDE.md / SKILL.md / README 等)
- 决定阶段数(4-7,太多用户疲劳)
- 定每阶段输入(用户填什么)+ 输出(AI 输出什么格式)

### 2. Prompt 设计
- 每个 stage 一个 prompt,头部明确"你是 X 阶段"
- 输出格式机器可解析(优先 JSON,fallback markdown code block)
- 阶段切换时 prompt 必须包含"上阶段输出摘要"

### 3. 实现
- 主对话流 + 阶段进度条 UI
- AI 回复实时解析(边显示边提取)
- PATCH 建议以 diff 卡片展示,用户三态选择
- 阶段完成 → 自动保存到 localStorage,刷新可继续

### 4. 修补审查(关键)
- 交叉审查两个文件的一致性(CLAUDE.md 提到的工具,SKILL.md 是否都有)
- 触发/反触发是否矛盾(如同时"用于 Python"和"不用于 Python")
- 覆盖操作是否完整(7 阶段是否每个都对应覆盖操作)
- 高严重度问题必须用户确认才能导出

### 5. 导出
- 用户审阅通过 → 导出文件(单文件 / zip)
- 保留生成历史,支持回看/重新生成
- 提供"重新跑阶段 N"的回退入口

## 交付清单(checklist)

- [ ] 4-7 阶段流程清晰
- [ ] 每阶段 UI 进度可见
- [ ] `[STAGE:N]` 解析 + 自然语言 fallback
- [ ] 代码块/PATCH JSON 解析稳定
- [ ] 修补建议三态 UI
- [ ] 生成后自检(一致性 + 矛盾)
- [ ] 历史记录 + 重新生成入口
- [ ] 导出支持多文件 zip
