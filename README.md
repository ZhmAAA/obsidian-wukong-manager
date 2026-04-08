# Obsidian-WuKongManager

> Obsidian 知识库管理 Skill —— 为 AI Agent 提供原生 Obsidian 操作能力

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://www.python.org)
[![Version](https://img.shields.io/badge/Version-v1.0-blue)]()

---

## 🔥 解决什么问题

用 AI Agent 管理笔记时，常见的困境：

- AI 生成的笔记格式随意，不符合 Obsidian 规范（缺少 Front Matter、双链写错）
- 想生成知识图谱/看板，手动复制粘贴费时费力
- 笔记一多就找不到，没有结构化管理体系

**Obsidian-WuKongManager** 把 Obsidian 规范封装成可调用的 Skill 和脚本，让 AI Agent 能够：
- 生成**格式正确的** Markdown 笔记（含 Front Matter、标签、双链）
- 创建**符合规范的** Canvas 画布（思维导图、流程图、知识图谱）
- 生成**可直接使用的**数据库视图（Table、Kanban、Index）

---

## ✨ 核心能力

### 1. Markdown 笔记管理

生成符合 Obsidian 规范的笔记文件：

- **Front Matter** — `title`、`created`、`tags`、`aliases`、`description`
- **双链语法** — `[[笔记]]`、`[[笔记|显示文本]]`
- **嵌入语法** — `![[笔记]]`
- **Callout 提示块** — `> [!note]`、`> [!warning]`、`> [!todo]`

### 2. Canvas 画布

创建 Obsidian Canvas 格式的可视化图形：

- **节点类型** — text、file、link、group
- **颜色支持** — blue、green、yellow、orange、red、purple、gray、pink
- **边连接** — 带标签的双向连接线

### 3. 数据库视图

生成 Dataview 插件格式的结构化数据视图：

- **Table View** — Markdown 表格 + Dataview 查询
- **Index View** — YAML 元数据 + Dataview 查询
- **Kanban View** — Markdown 待办分组看板

---

## 📦 环境要求

| 依赖 | 版本要求 | 说明 |
|------|----------|------|
| Python | 3.8+ | 运行脚本工具 |
| Obsidian | 任意版本 | 笔记仓库 |
| Dataview 插件 | 推荐安装 | 数据库视图需要 |

> 无需安装任何第三方依赖，脚本仅使用 Python 标准库。

---

## 🚀 快速开始

### 方式一：作为 AI Agent Skill 使用

将 `SKILL.md` 内容复制到 AI Agent 的 Skill 输入框中，直接用自然语言描述需求：

```
用户：帮我创建一篇关于 AI Agent 的笔记，包含双链和标签
助手：调用 obsidian-wukong-manager skill，生成符合规范的 Obsidian 笔记
```

### 方式二：直接使用 Python 脚本

```bash
# 克隆仓库
git clone https://github.com/ZhmAAA/obsidian-wukong-manager.git
cd obsidian-wukong-manager

# 创建笔记
python scripts/create_note.py \
  --vault /path/to/vault \
  --title "AI Agent 入门指南" \
  --tags "AI,Agent,入门"

# 创建画布
python scripts/create_canvas.py \
  --vault /path/to/vault \
  --title "工作流" \
  --nodes '[]' \
  --edges '[]'

# 创建数据表
python scripts/create_database.py \
  --vault /path/to/vault \
  --type table \
  --title "项目列表" \
  --headers "名称,状态,优先级" \
  --rows '[["项目A","进行中","高"],["项目B","待办","中"]]'
```

### 方式三：集成到 Wukong Agent

将整个项目文件夹复制到悟空 Agent 的 `skills` 目录即可。

---

## 📂 项目结构

```
obsidian-wukong-manager/
├── SKILL.md                      # Skill 主文件（供 AI Agent 使用）
├── README.md                     # 项目说明文档
├── LICENSE                       # MIT 许可证
├── requirements.txt              # 依赖说明（仅标准库，无需安装）
├── scripts/                      # Python 脚本工具
│   ├── create_note.py            # 创建 Markdown 笔记
│   ├── create_canvas.py          # 创建 Canvas 画布
│   ├── create_database.py        # 创建数据库视图
│   └── cleanup.py                # 清理工具
├── references/                   # 参考文档
│   └── obsidian-syntax.md        # Obsidian 语法速查
└── examples/                     # 示例文件
    ├── sample-note.md            # 笔记示例
    └── sample-canvas.canvas      # Canvas 示例
```

---

## 🎬 使用示例

### 创建笔记

```python
from scripts.create_note import create_note

filename, filepath = create_note(
    vault_path="/path/to/vault",
    title="AI Agent 入门指南",
    content="## 什么是 AI Agent\n\nAI Agent 是...",
    tags=["AI", "Agent"]
)
# 生成文件：AI Agent 入门指南.md
```

### 创建画布

```python
from scripts.create_canvas import create_canvas, add_text_node, add_edge

nodes = [
    add_text_node("1", "开始", x=0, y=0, color="green"),
    add_text_node("2", "执行", x=300, y=0, color="blue"),
    add_text_node("3", "完成", x=600, y=0, color="purple")
]

edges = [
    add_edge("1", "2", label="执行任务"),
    add_edge("2", "3", label="返回结果")
]

create_canvas("/path/to/vault", "工作流", nodes, edges)
```

---

## 📖 相关资源

- [Obsidian 官方文档](https://help.obsidian.md/)
- [Dataview 插件](https://blacksmithgu.github.io/obsidian-dataview/)
- [Canvas 文档](https://help.obsidian.md/Canvas)
- [Wukong-Ruyi](https://github.com/ZhmAAA/wukong-ruyi) — 悟空 Agent 外挂增强系统

---

## 🤝 贡献指南

### 技术栈

- **Python 3.8+** — 脚本工具
- **Obsidian** — 知识库格式
- **Dataview** — 数据库查询（可选）

### 开发规范

1. 脚本仅使用 Python 标准库，不引入外部依赖
2. 新增脚本需要包含 `--help` 参数说明
3. 提交前确保 `python scripts/*.py --help` 可正常运行

### Pull Request 流程

1. Fork 本仓库
2. 创建特性分支 `git checkout -b feature/xxx`
3. 开发并测试
4. 提交 `git commit -m 'feat: add xxx'`
5. 推送并创建 Pull Request

---

## ⚠️ 免责声明

1. 本项目与 Obsidian 官方无关联，仅为个人工具开发
2. 使用本项目造成的任何数据丢失，由使用者自行承担
3. 请勿在生产环境 vault 上直接测试，建议先备份或使用测试库

---

## 📄 License

MIT License - 详见 [LICENSE](LICENSE) 文件

---

**Obsidian-WuKongManager v1.0** — 让 AI 帮你管理 Obsidian 知识库。

*如果对你有帮助，请给个 ⭐ Star！*
