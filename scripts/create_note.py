#!/usr/bin/env python3
"""创建 Obsidian Markdown 笔记"""
import os
import sys
import json
import argparse
from datetime import datetime

def create_note(vault_path, title, content="", tags=None, frontmatter=None):
    """创建 Obsidian 笔记"""
    # 处理标题作为文件名
    safe_filename = "".join(c if c.isalnum() or c in " -_" else "_" for c in title)
    filename = f"{safe_filename}.md"
    filepath = os.path.join(vault_path, filename)
    
    # 构建 Front Matter
    fm_parts = ["---"]
    fm_parts.append(f"title: {title}")
    fm_parts.append(f"created: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    if tags:
        if isinstance(tags, list):
            fm_parts.append(f"tags: [{', '.join(tags)}]")
        else:
            fm_parts.append(f"tags: [{tags}]")
    if frontmatter:
        for key, value in frontmatter.items():
            fm_parts.append(f"{key}: {value}")
    fm_parts.append("---")
    
    # 构建完整内容
    full_content = "\n".join(fm_parts) + "\n\n"
    if content:
        full_content += content
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(full_content)
    
    return filename, filepath

def main():
    parser = argparse.ArgumentParser(description="创建 Obsidian 笔记")
    parser.add_argument("--vault", required=True, help="Vault 路径")
    parser.add_argument("--title", required=True, help="笔记标题")
    parser.add_argument("--content", default="", help="笔记内容")
    parser.add_argument("--tags", help="标签（逗号分隔）")
    args = parser.parse_args()
    
    tags = args.tags.split(",") if args.tags else None
    filename, filepath = create_note(args.vault, args.title, args.content, tags)
    
    print(f"Created: {filename}")
    print(f"Path: {filepath}")

if __name__ == "__main__":
    main()
