# local-standalone-html-app

## 触发条件
需要交付零依赖、无需安装、双击即用的本地工具时使用。所有逻辑、样式、字体引用集中在单一 HTML 文件，状态用原生 JS 对象管理，持久化用 localStorage，UI 用 CSS Variable 主题化。

## 反触发
- 需要多页面路由时
- 需要 Node.js / 文件系统访问时
- 团队协作需要版本控制的组件库时

## 覆盖操作
- CSS Variable 设计系统
- 原生 DOM 操作替代框架
- localStorage 读写封装
- 模态框/侧边栏/对话气泡的纯 CSS 实现
