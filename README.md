# Obsidian-WuKongManager

Obsidian vault 管理技能，为悟空 Agent 提供原生 Obsidian 操作能力。

## 功能特性

### 1. Markdown 笔记管理

**语法支持：**
- 双链：`[[笔记标题]]`, `[[笔记|显示文本]]`
- 嵌入：`![[笔记标题]]`
- 标签：`#标签`, `#分类/子标签`
- Callout：`> [!note] 内容`

### 2. Canvas 画布

创建思维导图、知识图谱、流程图。支持节点类型：text、file、link、group。

### 3. 数据库视图

三种视图类型：
- **Table View**: Dataview 格式 Markdown 表格
- **Index View**: YAML + Dataview 查询
- **Kanban View**: Markdown 待办分组看板

## 安装

### 方法一：克隆仓库

```bash
git clone https://github.com/zarazhangrui/obsidian-wukong-manager.git
cd obsidian-wukong-manager
```

### 方法二：集成到 Wukong Agent

将该技能文件夹复制到 Wukong 的 skills 目录即可使用。

## 使用方法

### 命令行工具

```bash
# 创建笔记
python scripts/create_note.py --vault /path/to/vault --title "我的笔记" --tags "AI,创业"

# 创建画布
python scripts/create_canvas.py --vault /path/to/vault --title "项目画布" --nodes '[]' --edges '[]'

# 创建数据库视图
python scripts/create_database.py --vault /path/to/vault --type table --title "数据表" --headers "名称,状态" --rows '[["项目A","进行中"]]'
```

### 作为 Wukong Skill 使用

```
用户：创建一篇关于 AI Agent 的笔记
助手：调用 obsidian-wukong-manager skill，自动生成符合 Obsidian 规范的笔记文件
```

## 项目结构

```
obsidian-wukong-manager/
├── SKILL.md                    # 技能主文件
├── README.md                   # 本文件
├── LICENSE                     # MIT 许可证
├── scripts/                    # Python 脚本工具
│   ├── create_note.py          # 创建笔记
│   ├── create_canvas.py        # 创建画布
│   ├── create_database.py      # 创建数据库视图
│   └── cleanup.py              # 清理工具
├── references/                 # 参考文档
│   └── obsidian-syntax.md       # Obsidian 语法参考
└── examples/                   # 示例文件
    ├── sample-note.md
    └── sample-canvas.canvas
```

## 示例

### 创建笔记

```python
from scripts.create_note import create_note

filename, filepath = create_note(
    vault_path="/path/to/vault",
    title="AI Agent 笔记",
    content="## 什么是 AI Agent\n\nAI Agent 是...",
    tags=["AI", "Agent"]
)
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

## 相关资源

- [Obsidian 官方文档](https://help.obsidian.md/)
- [Dataview 插件](https://blacksmithgu.github.io/obsidian-dataview/)
- [Canvas 文档](https://help.obsidian.md/Canvas)

## 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 作者

张黄铭 [@zhanghuangming](https://github.com/zhanghuangming)
