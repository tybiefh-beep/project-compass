---
name: ai-provider-api-integration
description: 浏览器端直接调用多家 AI 提供商 REST API 的统一集成方案——Anthropic / OpenAI 兼容 / Gemini 三种格式的请求构建、响应解析、错误处理、API Key 浏览器端安全存储。Use when user wants multi-model chat, provider abstraction, browser-side API call, unified LLM client. Triggers: 多模型接入、AI 提供商、统一 LLM 客户端、Anthropic 集成、OpenAI 兼容、Gemini 调用、API Key 存储、模型切换。
license: MIT
metadata:
  author: 迷途绿意
  version: "3.1"
---

# ai-provider-api-integration

## 触发条件

需要在前端直接调用多家 AI 提供商 REST API 时使用。包括 Anthropic / OpenAI 兼容格式 / Gemini 特殊格式的请求构建、响应解析、错误处理、API Key 的浏览器端安全存储,以及模型可用性实时验证。

## 反触发(不适用)

- 后端代理架构下不使用(API Key 应放服务端)
- 仅调用单一提供商时过度设计(直接 fetch 即可)
- 涉及流式输出(SSE)时需另行处理
- 企业级生产环境(应走官方 SDK + 监控)

## Gotchas(易错点)

- **Anthropic 用 `x-api-key` header,OpenAI 用 `Authorization: Bearer`** → 抽象成 `buildHeaders(provider, key)`,别让业务层关心
- **Gemini 把 key 塞 query string** → `?key=xxx`,不是 header;同时 `safetySettings` 数组结构跟另两家完全不同
- **Anthropic 的 system 参数是顶层,OpenAI 是 messages[0].role='system'** → 别混
- **Anthropic 返回 content 是数组** → `response.content[0].text`;OpenAI 是 `response.choices[0].message.content`;Gemini 是 `response.candidates[0].content.parts[0].text`
- **流式 vs 非流式 content 路径不同** → 非流式直接读 `.content`;流式要 `ReadableStream` 读 `data: {...}\n\n` 增量拼
- **错误信息三家人结构差很大** → 统一抽象 `parseError(provider, status, body)` → 返回 `{ code, message, retryable }`
- **API Key 放 localStorage 已被同源脚本可读** → 接受这个限制(浏览器没更安全方案),但加 domain 校验和 CSP 头防 XSS 偷
- **CORS 跨域**:Anthropic 允许 `anthropic-dangerous-direct-browser-access: true` header(2024 年新增),OpenAI 默认不允许,需代理

## 覆盖操作(必须支持)

- [ ] Provider 配置对象设计(URL / header style / body schema / response path)
- [ ] headers 构建(按 provider 分发)
- [ ] buildBody 差异处理(Anthropic vs OpenAI vs Gemini)
- [ ] parseReply 统一抽象(三家不同返回路径 → 统一 string 输出)
- [ ] verifyModel 最小 token 验证(发"hi"看是否 200)
- [ ] localStorage 持久化 + 加密(可选 AES,key 由用户密码派生)
- [ ] 模型版本列表维护(推荐/预览/旧版标注)
- [ ] 错误重试策略(429/5xx 指数退避,4xx 直接报错)
- [ ] Token 用量统计(从 response.usage 提取)

## 工作流(分阶段)

### 1. 立项
- 列出要支持的 provider(2-8 家为宜)
- 决定是否流式(SSE)
- 决定是否多模态(图/文/音)

### 2. 数据设计
- Provider 配置:`{ id, name, baseUrl, authStyle, requestSchema, responseSchema, models[] }`
- 统一请求接口:`{ provider, model, messages, system, temperature, maxTokens, stream }`
- 统一响应接口:`{ content, usage, model, raw }`

### 3. 实现
- Provider 注册表(数组,新增 provider 加一项即可)
- `dispatch(provider, request)` 单一入口
- 三家 SDK 调用代码各放一个文件,业务层不感知差异
- 错误归一化(用户只看到"调用失败"+"原始错误")

### 4. 测试
- 每个 provider 至少 1 个正常调用 + 1 个错误路径
- Key 失效 → UI 明确提示
- 跨域失败 → 提示需要代理
- 流式中断 → 友好降级到非流式

## 交付清单(checklist)

- [ ] 至少支持 2-3 家 provider
- [ ] Provider 注册表化(新增 1 家 ≤ 50 行代码)
- [ ] 统一请求/响应接口
- [ ] verifyModel 一键验证
- [ ] API Key localStorage 存储 + 加密可选
- [ ] 错误信息用户友好(不暴露 stack)
- [ ] 模型版本可维护(推荐/预览/旧版标注)
- [ ] 至少 1 个 provider 流式输出
