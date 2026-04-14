#  高效学习助手 (Efficient Learning Assistant)

> 用生活化例子和可视化，让任何知识都能快速掌握

[English](#english) | 中文

---

## 这是什么

高效学习助手是一个**学习增强型 SKILL**，当你需要理解任何概念时使用。它通过多模态学习方式帮你建立深度理解：

- 🌟 **生活化例子** - 用熟悉的场景解释抽象概念
- 📚 **通俗讲解** - 大白话讲清楚复杂原理
- 🧠 **记忆口诀** - 快速记忆的技巧和联想
- 📊 **可视化图示** - SVG 图表帮你建立直观认知

最终生成**精美的交互式 HTML 学习笔记**，支持打印和离线查看。

---

## 1、快速开始

### 触发方式

说出你的学习需求：

```
"帮我学习一下 [概念]"
"解释一下 [知识点]"
"怎么理解 [原理]"
"给我举个例子说明 [概念]"
"画个图说明 [过程]"
```

### 输出示例

输入：`请解释一下MCP`

输出：一份包含 3 个生活例子、概念讲解、记忆口诀、调用栈图示的完整学习笔记


---

## 2、项目结构

```
efficient-learning/
├── agents/                 # 技能元数据
│   ├── skill.json         # 名称、描述、触发词等
│   └── config.schema.json # 配置项定义
├── templates/             # HTML 模板
│   └── learning_template.html
├── references/            # 参考文档
│   ├── learning_methods.md
│   └── svg_templates.md
├── scripts/               # 工具脚本
│   └── generate_learning_note.py
├── examples/              # 示例输出
├── .gitignore
├── README.md
└── SKILL.md              # 核心技能文档
```

---

## 3、核心特性

| 特性 | 说明 |
|-----|------|
| **多模态学习** | 例子 + 讲解 + 记忆法 + 图示，全方位认知加工 |
| **精美排版** | 渐变封面、卡片布局、交互动画、响应式设计 |
| **打印友好** | 专门优化打印样式，可导出 PDF |
| **开箱即用** | 无需配置，直接触发使用 |
| **可扩展** | 支持练习题、知识关联、学习路径等扩展模块 |

---

## 4、使用方法

### 1） 基础使用

直接描述你的学习需求：

- 技术概念：`帮我学习一下什么是缓存穿透`
- 科学原理：`解释一下光合作用`
- 商业理论：`怎么理解沉没成本`
- 数学公式：`给我讲讲贝叶斯定理`

### 2） 输出位置

学习笔记默认生成在用户工作目录，文件命名：

```
[概念名]_学习笔记.html
```

### 3） 查看方式

- 用浏览器打开 HTML 文件
- 支持滚动阅读、导航跳转
- 按 `Ctrl+P` 可打印为 PDF

---

## 5、内容模块

生成的学习笔记包含以下模块：

### 必含模块

1） **生活化例子** (2-4个)
   - 贴近日常的场景类比
   - 从简单到复杂递进

2） **概念讲解**
   - 一句话定义
   - 通俗解释
   - 核心要点
   - 常见误区

3） **简单记法**
   - 口诀、联想、首字母缩写
   - 记忆宫殿、故事串联

4） **可视化图示**
   - 流程图、树状图、关系图
   - SVG 矢量图，清晰可缩放

### 可选模块

- **知识关联** - 前置知识、延伸学习、相关概念
- **实战练习** - 基础/进阶/挑战题
- **速查卡片** - 可打印的核心要点

---

## 6、配置说明

通过 `agents/config.schema.json` 可自定义：

```json
{
  "output": {
    "format": "html",        // 输出格式
    "theme": "default",      // 主题风格
    "save_directory": "./output"
  },
  "content": {
    "example_count": 3,      // 例子数量
    "include_diagrams": true, // 是否包含图示
    "include_exercises": false
  }
}
```

---

## 7、示例展示

### 示例 1：递归 (Recursion)

- **例子**：俄罗斯套娃、查字典、盗梦空间
- **核心**：函数调用自身，递+归两个过程
- **口诀**："Trust the Process"
- **图示**：调用栈展开过程


### 示例 2：MCP 协议

- **例子**：USB-C 接口、餐厅点餐、翻译官
- **核心**：AI 世界的通用连接标准
- **口诀**："Model 连 Context 靠 Protocol"
- **图示**：架构图、对比图、时间线

---


<a name="english"></a>

# Efficient Learning Assistant

> Learn any concept faster with relatable examples and visualization

---

##  What is this

A **learning-enhancement SKILL** that helps you understand any concept through multi-modal learning:

- 🌟 **Relatable Examples** - Explain abstract concepts with familiar scenarios
- 📚 **Plain Explanations** - Complex ideas in simple words
- 🧠 **Memory Tricks** - Mnemonics and associations for quick recall
- 📊 **Visual Diagrams** - SVG charts for intuitive understanding

Generates **beautiful interactive HTML learning notes**.

---

##  Quick Start

### Trigger Phrases

```
"Help me learn [concept]"
"Explain [topic]"
"How to understand [principle]"
"Give me an example of [concept]"
"Draw a diagram of [process]"
```

---

##  Content Modules

1. **Examples** (2-4 relatable scenarios)
2. **Concept Explanation** (definition + key points + misconceptions)
3. **Memory Aids** (mnemonics + associations)
4. **Visual Diagrams** (flowcharts, mind maps, comparison tables)

---

##  Configuration

Customize via `agents/config.schema.json`:

```json
{
  "output": {
    "format": "html",
    "theme": "default"
  },
  "content": {
    "example_count": 3,
    "include_diagrams": true
  }
}
```

---

**Made with ❤️ for lifelong learners**
