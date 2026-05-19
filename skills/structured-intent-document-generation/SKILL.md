# structured-intent-document-generation

## 触发条件
需要通过对话引导用户将项目意图和技能知识结构化输出为 CLAUDE.md 或 SKILL.md 文件时使用。包括多阶段对话流程设计、stage 标记解析、文件内容从 AI 回复中提取、修补建议的监督式采纳流程。

## 反触发
- 用户直接提供完整文档无需生成时
- 纯问答场景不涉及文件输出时

## 覆盖操作
- SYSTEM_PROMPT 设计
- `[STAGE:N]` 解析与 UI 联动
- 正则提取 markdown/xml 代码块
- PATCH JSON 单行解析
- patch 采纳/拒绝/修改的三态 UI 与内容回写
