# Project Compass

<div align="center">

![GitHub Stars](https://img.shields.io/github/stars/tybiefh-beep/project-compass?style=flat-square)
![GitHub Forks](https://img.shields.io/github/forks/tybiefh-beep/project-compass?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)
![HTML](https://img.shields.io/badge/HTML-Pure%20Browser-orange?style=flat-square)

**Transform chaotic project ideas into actionable direction in 4 questions. Auto-generate CLAUDE.md + SKILL.md.**

Double-click HTML to use | Zero dependencies | Pure browser | API keys stay local

[🚀 Quick Start](#quick-start) · [✨ Features](#features) · [📖 Detailed Guide](#7-stage-workflow) · [中文](./README.md)

</div>

---

## 🎯 What is This?

**Project Compass** is a single-file HTML tool that helps you clarify chaotic project ideas. Using just 4 key questions, it automatically generates two essential files for Claude Code:

- **CLAUDE.md** — Project operation manual that tells AI how your project works and what to watch for
- **SKILL.md** — Skill definition file that triggers specialized AI behaviors in specific scenarios

### Why Choose It?

| Challenge | Traditional | Project Compass |
|-----------|-----------|------------------|
| How to start? | Install Node.js, npm deps... | Double-click HTML file ✅ |
| API key security? | Upload to server ❌ | Stored locally, never uploaded ✅ |
| AI model support? | Usually single provider | 8+ model vendors ✅ |
| Learning curve | Steep | Conversational guidance ✅ |

---

## 🚀 Quick Start

### Method 1: Download (Recommended)

1. **Download** the `claude-skill 生成器.html` file
   ```
   • Click the Files tab
   • Find claude-skill 生成器.html
   • Right-click → Save Link As
   ```

2. **Open** - Double-click the file and your browser opens it automatically

3. **Verify** - Enter your API Key and click "Verify"

4. **Start Generating** - Click "➕ New Project"

### Method 2: Online Version (Coming Soon)

> Pure online version under development, no download needed

---

## 💻 Usage Flow

### Step 1: Configure AI Provider

```
Left sidebar → Select provider → Enter API Key → Click "Verify"
```

✅ **Supported Models:**

| Provider | Available Models |
|----------|------------------|
| **Claude** (Anthropic) | Opus 4.7 / Sonnet 4.6 / Haiku 4.5 |
| **GPT** (OpenAI) | GPT-4.1 / GPT-4o / o3-mini |
| **DeepSeek** | deepseek-chat / reasoner / coder |
| **Alibaba QianWen** | qwen-max / plus / turbo |
| **Zhipu GLM** | glm-4-plus / flash |
| **Gemini** (Google) | gemini-2.5-pro / flash |
| **Moonshot** | moonshot-v1 series |
| **Custom** | Any OpenAI-compatible interface |

### Steps 2-7: Auto-Generation

After clicking "➕ New Project", the system executes these stages:

| Stage | ⏱️ Time | What it Does |
|-------|--------|-----------------------------------------------|
| 1️⃣ Project Description | ~1 min | Understand you, your project, and pain points |
| 2️⃣ Tool Architecture Analysis | ~2 min | Map tools → match best practices → architecture |
| 3️⃣ Automation Identification | ~1 min | Recommend automation strategies, AI vs manual |
| 4️⃣ CLAUDE.md Generation | ~2 min | Generate project operation manual |
| 5️⃣ SKILL.md Extraction | ~1 min | Identify and generate skill definitions |
| 6️⃣ Cross-Review | ~1 min | Verify consistency across files |
| 7️⃣ Files Ready | - | Download and export |

**Total time**: ~8-10 minutes, end-to-end.

---

## ✨ Features

### Core Features

- ✅ **Conversational Guidance** - 4 key questions clarify your thinking
- ✅ **Auto-generate CLAUDE.md** - Project manual one-click generation
- ✅ **Auto-extract SKILL.md** - Skill definitions auto-analyzed
- ✅ **7-Stage Workflow** - From chaos to actionable documentation

### Advanced Features

- 🌙 **Dark/Light Mode** - Auto-switches to your environment, preference remembered
- 📎 **File Upload** - Support .md / .json / .yaml / .txt for context
- 🔧 **Self-Optimization** - AI reviews and improves the generator itself
- 💾 **Session Management** - Generation history saved, review or edit anytime

### Privacy & Security

- 🔒 **Local Storage** - API keys in browser localStorage, never uploaded
- 🌐 **Direct API Connection** - All requests from browser to AI vendors, no intermediary
- 📵 **Zero Tracking** - No user data collection or usage statistics

---

## 📚 Use Cases

### 📱 Web Application Developers

**Scenario**: Building a new React Dashboard, want Claude Code help for rapid iteration  
**Benefit**: Generate CLAUDE.md describing project structure, component standards, state management  
**Result**: Claude Code generates code matching your standards perfectly ✅

### 🐍 Python Tool Maintainers

**Scenario**: Maintaining multiple CLI tools, want to automate parts of workflow  
**Benefit**: Define automation rules via SKILL.md, tell Claude when to trigger tests/deployment  
**Result**: Reduce manual checks by 50% ✅

### 🤖 AI Workflow Designers

**Scenario**: Designing complex multi-step prompt workflows  
**Benefit**: Use Project Compass to clarify workflow stages and trigger conditions  
**Result**: Generate standardized SKILL.md files for direct use in Claude Code ✅

---

## 🏗️ Project Structure

```
project-compass/
├── claude-skill 生成器.html    # 📦 Main program (single file, ready to use)
├── skills/                      # 📚 7 built-in SKILL.md templates
│   ├── ai-failure-pattern-collector/
│   ├── ai-persistent-memory-system/
│   ├── ai-provider-api-integration/
│   ├── ai-reasoning-process-visualizer/
│   ├── local-standalone-html-app/
│   ├── self-evolving-prompt-system/
│   └── structured-intent-document-generation/
├── generated/                   # 📄 Example outputs (reference)
├── README.md                    # 📖 Chinese documentation
├── README_EN.md                 # 📖 English documentation
└── docs/                        # 📋 Detailed guides (in progress)
```

---

## ⚙️ Technical Details

### Compatibility

- **Browsers** - Chrome, Firefox, Safari, Edge (latest versions recommended)
- **Systems** - Windows, macOS, Linux (any system with a browser)
- **Models** - Any OpenAI-compatible API format

### Known Limitations

- ⚠️ Some models don't support `[STAGE:N]` format markers; tool auto-detects and alerts
- 💡 **Recommended**: Claude Opus / GPT-4 series for optimal generation quality

### Getting API Keys

| Provider | Apply Link |
|----------|----------|
| Claude | https://console.anthropic.com |
| OpenAI | https://platform.openai.com/api-keys |
| DeepSeek | https://platform.deepseek.com |
| Alibaba QianWen | https://dashscope.console.aliyun.com |
| Zhipu GLM | https://open.bigmodel.cn |
| Gemini | https://aistudio.google.com |
| Moonshot | https://platform.moonshot.cn |

---

## 🔒 Privacy Policy

- ✅ **Zero Upload** - API keys and all data stored locally in your browser
- ✅ **Direct API** - No intermediary servers; requests go directly to AI vendors
- ✅ **Offline Ready** - After setup, even without internet you can view past generated files

---

## �� FAQ

### Q: Can I share the downloaded HTML file with others?

**A**: Absolutely! It's a single-file app—everyone can use it independently with no conflicts.

### Q: Will my API key be uploaded?

**A**: No. All keys are stored in browser localStorage only, never leaving your device.

### Q: Can I use it offline?

**A**: Not fully—you need internet to call AI APIs. However, all data processing happens locally; only API calls need connectivity.

### Q: Can I use the generated files directly?

**A**: Yes, ~95% of the time. The other 5% might need minor tweaks for your specific project. We recommend reviewing first.

### Q: Can I improve generation results?

**A**: Yes! The tool provides an "Edit" feature where you can modify any generated content anytime.

---

## 🎁 Built-in SKILL Templates

The tool comes with 7 professional SKILL.md templates covering:

1. **AI Failure Pattern Collector** - Log AI errors to avoid repeats
2. **AI Persistent Memory System** - Cross-session memory management
3. **AI Provider API Integration** - Multi-model API interface standards
4. **AI Reasoning Process Visualizer** - Chain-of-thought display
5. **Local Standalone HTML Application** - Standalone HTML tool standards
6. **Self-Evolving Prompt System** - Prompt versioning and optimization
7. **Structured Intent Document Generation** - Auto document generation workflow

---

## 🤝 Contributing

We welcome Issues and Pull Requests! Especially interested in:

- 🐛 Bug reports and fixes
- ✨ New SKILL template proposals
- 🌍 Language translations
- 📚 Documentation improvements

---

## 📜 License

MIT License - Free to use, modify, and distribute

---

## 💬 Feedback & Contact

- 📧 Discussions - [GitHub Issues](https://github.com/tybiefh-beep/project-compass/issues)
- 💭 Ideas - [GitHub Discussions](https://github.com/tybiefh-beep/project-compass/discussions)

---

<div align="center">

**⭐ If you find this helpful, please give it a Star!**

Made with ❤️ by [tybiefh-beep](https://github.com/tybiefh-beep)

[⬆ Back to Top](#project-compass)

</div>
