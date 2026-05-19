# ai-provider-api-integration

## 触发条件
需要在前端直接调用多家 AI 提供商 REST API 时使用。包括 Anthropic / OpenAI 兼容格式 / Gemini 特殊格式的请求构建、响应解析、错误处理、API Key 的浏览器端安全存储，以及模型可用性实时验证。

## 反触发
- 后端代理架构下不使用
- 仅调用单一提供商时过度设计
- 涉及流式输出（SSE）时需另行处理

## 覆盖操作
- Provider 配置对象设计
- headers 构建
- buildBody 差异处理（Anthropic vs OpenAI vs Gemini）
- parseReply 统一抽象
- verifyModel 最小 token 验证
- localStorage 持久化
- 模型版本列表维护（推荐/预览/旧版标注）
