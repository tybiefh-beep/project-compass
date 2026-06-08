---
name: local-standalone-html-app
description: 交付零依赖、双击即用的单文件 HTML 工具——所有逻辑/样式/字体集中在一个文件,localStorage 状态,CSS Variable 主题化,纯浏览器运行。Use when user wants standalone offline tool, single-file HTML deliverable, no Node.js, no build step, double-click to run, no installation. Triggers: 本地工具、单文件 HTML、离线工具、双击运行、零依赖、不用安装。
license: MIT
metadata:
  author: 迷途绿意
  version: "3.1"
---

# local-standalone-html-app

## 触发条件

需要交付零依赖、无需安装、双击即用的本地工具时使用。所有逻辑、样式、字体引用集中在单一 HTML 文件,状态用原生 JS 对象管理,持久化用 localStorage,UI 用 CSS Variable 主题化。

## 反触发(不适用)

- 需要多页面路由时
- 需要 Node.js / 文件系统访问时
- 团队协作需要版本控制的组件库时
- 需要后端 API / 数据库时
- 用户明确要求"做成 web 应用"时(此时用 Next.js/Vue 等)

## Gotchas(易错点)

- **CDN 字体断网就废了** → 优先用 `system-ui, -apple-system, sans-serif` 系统字体栈;非要装饰字体,内嵌 base64 或提供离线 fallback
- **localStorage 写 object 会被 toString 成 `[object Object]`** → 写时 `JSON.stringify(val)`,读时 `JSON.parse(str)`,封装成 `ls/lset/lremove` 三个 helper
- **CSS Variable 主题切换不生效** → 变量定义必须在 `:root`(亮)和 `:root[data-theme="dark"]`(暗)两处都写,JS 切换时改 `document.documentElement.dataset.theme`
- **内嵌 JS/CSS 体积爆炸** → 单文件 < 200KB 是合理目标;超过 500KB 考虑拆成多文件或换方案
- **iOS Safari 100vh 含地址栏高度** → 用 `100dvh` 或 `vh + calc(地址栏高度)` 兼容
- **第三方 CDN 库(Papa Parse/Marked 等)要锁版本号** → `https://cdn.jsdelivr.net/npm/marked@12.0.0/marked.min.js`,不能 `latest`

## 覆盖操作(必须支持)

- [ ] CSS Variable 设计系统(`--bg`/`--text`/`--accent` 等 8-12 个核心变量)
- [ ] 亮/暗主题切换(偏好存 localStorage,启动时读取)
- [ ] 原生 DOM 操作替代框架(用 `document.createElement` + 事件委托)
- [ ] localStorage 读写封装(JSON 序列化 + try/catch)
- [ ] 模态框/侧边栏/对话气泡的纯 CSS 实现(不用第三方 UI 库)
- [ ] 响应式布局(mobile-first,`flex` + `grid` 为主,断点 768/1024)
- [ ] 键盘快捷键(`Esc` 关闭弹窗、`Enter` 提交等)
- [ ] 错误展示在 UI 内,不用 `alert`(阻断感强)

## 工作流(分阶段)

### 1. 立项
- 一句话定位工具("解决 XX 问题,给 XX 人用")
- 列出 3-5 个核心功能
- 决定是否需要持久化(localStorage / 纯内存)

### 2. 设计
- 选 2-3 个参考工具,提取 UI 风格
- 画信息架构图(几个区块、各自放什么)
- 决定主题色(亮/暗各 1 个,主色 + 强调色)
- 列交互清单(用户能做什么、得到什么反馈)

### 3. 实现
- HTML 骨架先写好(空容器 + className)
- CSS 变量定义在 `:root`
- 写基础交互(主题切换/弹窗/通知)
- 写核心业务逻辑(分阶段:简单 → 复杂)
- localStorage 封装在工具函数层
- 异常路径全部 try/catch + 用户友好提示

### 4. 自测
- 双击 HTML 直接打开能跑
- DevTools Console 无 error/warn
- 断网情况下不卡死(CDN 资源失败的 fallback)
- 清空 localStorage 后行为合理
- iPhone Safari 打开正常(如果目标用户含移动端)
- 键盘 Tab 顺序合理,焦点可见

## 交付清单(checklist)

- [ ] 单 HTML 文件,体积 < 200KB
- [ ] 双击可运行,无需任何依赖
- [ ] 无 console 错误/警告
- [ ] 亮/暗主题可切换,偏好记忆
- [ ] localStorage 数据可正常存取
- [ ] 至少 3 个用户场景走通
- [ ] README.md 含使用说明
