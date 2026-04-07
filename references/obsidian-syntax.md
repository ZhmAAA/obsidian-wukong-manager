# Obsidian 语法参考

## 1. 双链语法 (Wikilinks)

### 基础链接
```markdown
[[笔记标题]]              -- 链接到笔记
[[笔记标题|显示文本]]     -- 带显示文本的链接
```

### 嵌入内容
```markdown
![[笔记标题]]            -- 嵌入整个笔记
![[笔记标题#标题]]       -- 嵌入笔记中的特定标题
![[笔记标题#^区块ID]]     -- 嵌入特定区块
![[笔记标题|最大宽度]]    -- 带宽度的嵌入
```

## 2. 标签系统 (Tags)

### 基础标签
```markdown
#标签名                   -- 单个标签
#领域/子标签              -- 分层标签
#2024/项目/进度          -- 多级分层
```

### 属性标签
```markdown
#标签?                   -- 问号标记未完成
#标签!                   -- 感叹号标记重要
```

## 3. Front Matter (YAML 元数据)

```yaml
---
title: 笔记标题
created: 2024-01-15
tags: [标签1, 标签2]
aliases: [别名1, 别名2]
description: 笔记描述
---

正文内容...
```

## 4. Callouts (提示块)

```markdown
> [!note] 标题
> 内容...

> [!tip] 提示
> [!warning] 警告
> [!danger] 危险
> [!info] 信息
> [!quote] 引用
> [!example] 示例
> [!summary] 总结
> [!bug] 缺陷
> [!todo] 待办
```

## 5. Canvas 节点类型

### JSON 结构
```json
{
  "nodes": [
    {
      "id": "unique-id",
      "type": "text",
      "text": "节点内容",
      "x": 100,
      "y": 100,
      "width": 200,
      "height": 100,
      "color": "blue"
    },
    {
      "id": "file-node",
      "type": "file",
      "file": "path/to/note.md",
      "x": 400,
      "y": 100
    },
    {
      "id": "group-1",
      "type": "group",
      "text": "分组标题",
      "x": 100,
      "y": 300,
      "width": 400,
      "height": 200
    }
  ],
  "edges": [
    {
      "id": "e1",
      "fromNode": "node1",
      "toNode": "node2",
      "fromSide": "right",
      "toSide": "left"
    }
  ]
}
```

### 节点颜色
- `blue`, `green`, `yellow`, `orange`, `red`, `purple`, `gray`, `pink`

### 边样式
```json
{
  "fromSide": "top|bottom|left|right",
  "toSide": "top|bottom|left|right",
  "label": "连接标签",
  "color": "blue"
}
```

## 6. 数据库视图 (Dataview)

### 基础查询
````dataview
TABLE file.ctime, tags
FROM ""
WHERE tags CONTAINS "项目"
SORT file.ctime DESC
````

### 字段引用
```dataview
TABLE column1 AS "列1", column2 + column3 AS "合计"
FROM "文件夹"
WHERE status = "进行中"
```

### 内联字段
```markdown
任务名称:: 完成 Obsidian 笔记
完成日期:: 2024-01-15
状态:: 🟢 进行中
```
