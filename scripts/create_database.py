#!/usr/bin/env python3
"""创建 Obsidian 数据库视图文件（模拟 Dataview/Database插件格式）"""
import os
import json
import argparse
from datetime import datetime

def create_dataview_table(vault_path, title, headers, rows):
    """创建 Dataview 格式的数据库视图"""
    filename = f"{title}.md"
    filepath = os.path.join(vault_path, filename)
    
    # 构建 Markdown 表格
    lines = []
    lines.append(f"# {title}\n")
    lines.append(f"> 数据表视图 | 创建时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
    
    # 表头
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("| " + " | ".join(["---"] * len(headers)) + " |")
    
    # 数据行
    for row in rows:
        lines.append("| " + " | ".join(str(cell) for cell in row) + " |")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    
    return filename, filepath

def create_yaml_index(vault_path, db_name, fields, records):
    """创建 YAML 格式的索引文件"""
    filename = f"{db_name}-index.md"
    filepath = os.path.join(vault_path, filename)
    
    lines = ["---"]
    lines.append(f"title: {db_name}")
    lines.append("type: database")
    lines.append(f"created: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append(f"fields: [{', '.join(fields)}]")
    lines.append(f"records: {len(records)}")
    lines.append("---")
    
    lines.append(f"\n# {db_name}\n")
    lines.append(f"类型: 数据库视图")
    lines.append(f"字段数: {len(fields)}")
    lines.append(f"记录数: {len(records)}\n")
    
    lines.append("## 字段定义")
    for i, field in enumerate(fields):
        lines.append(f"- **{field}**: 字段 {i+1}")
    
    lines.append("\n## 数据预览")
    lines.append(f"```dataview")
    lines.append(f"TABLE {', '.join(fields)}")
    lines.append(f'FROM "{db_name}"')
    lines.append("```")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    
    return filename, filepath

def create_kanban_view(vault_path, title, columns):
    """创建看板视图"""
    filename = f"{title}-看板.md"
    filepath = os.path.join(vault_path, filename)
    
    lines = [f"# {title} - 看板\n"]
    lines.append(f"> 创建时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
    
    for column_name, items in columns.items():
        lines.append(f"## {column_name}\n")
        for item in items:
            lines.append(f"- [ ] {item}")
        lines.append("")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    
    return filename, filepath

def main():
    parser = argparse.ArgumentParser(description="创建 Obsidian 数据库视图")
    parser.add_argument("--vault", required=True, help="Vault 路径")
    parser.add_argument("--type", required=True, choices=["table", "index", "kanban"], help="视图类型")
    parser.add_argument("--title", required=True, help="标题")
    parser.add_argument("--headers", help="表头（逗号分隔）")
    parser.add_argument("--rows", help="数据行（JSON 数组）")
    parser.add_argument("--columns", help="看板列（JSON 对象）")
    args = parser.parse_args()
    
    if args.type == "table":
        headers = args.headers.split(",") if args.headers else []
        rows = json.loads(args.rows) if args.rows else []
        filename, filepath = create_dataview_table(args.vault, args.title, headers, rows)
    elif args.type == "kanban":
        columns = json.loads(args.columns) if args.columns else {}
        filename, filepath = create_kanban_view(args.vault, args.title, columns)
    else:
        fields = args.headers.split(",") if args.headers else []
        records = json.loads(args.rows) if args.rows else []
        filename, filepath = create_yaml_index(args.vault, args.title, fields, records)
    
    print(f"Created: {filename}")
    print(f"Path: {filepath}")

if __name__ == "__main__":
    main()
