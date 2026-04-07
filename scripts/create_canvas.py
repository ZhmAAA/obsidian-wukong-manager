#!/usr/bin/env python3
"""创建 Obsidian Canvas 画布"""
import os
import json
import argparse
from datetime import datetime

def create_canvas(vault_path, title, nodes=None, edges=None):
    """创建 Obsidian Canvas"""
    filename = f"{title}.canvas"
    filepath = os.path.join(vault_path, filename)
    
    canvas = {
        "nodes": nodes or [],
        "edges": edges or [],
        "style": {
            "background": "#ffffff"
        }
    }
    
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(canvas, f, ensure_ascii=False, indent=2)
    
    return filename, filepath

def add_text_node(id, text, x=0, y=0, width=200, height=100, color=None):
    """添加文本节点"""
    node = {
        "id": id,
        "type": "text",
        "text": text,
        "x": x,
        "y": y,
        "width": width,
        "height": height
    }
    if color:
        node["color"] = color
    return node

def add_file_node(id, file, x=0, y=0, width=200, height=100):
    """添加文件节点"""
    return {
        "id": id,
        "type": "file",
        "file": file,
        "x": x,
        "y": y,
        "width": width,
        "height": height
    }

def add_group_node(id, text, x=0, y=0, width=400, height=300, color=None):
    """添加分组节点"""
    node = {
        "id": id,
        "type": "group",
        "text": text,
        "x": x,
        "y": y,
        "width": width,
        "height": height
    }
    if color:
        node["color"] = color
    return node

def add_edge(from_id, to_id, label=None, color=None):
    """添加连接线"""
    edge = {
        "id": f"e_{from_id}_{to_id}",
        "fromNode": from_id,
        "toNode": to_id,
        "fromSide": "right",
        "toSide": "left"
    }
    if label:
        edge["label"] = label
    if color:
        edge["color"] = color
    return edge

def main():
    parser = argparse.ArgumentParser(description="创建 Obsidian Canvas")
    parser.add_argument("--vault", required=True, help="Vault 路径")
    parser.add_argument("--title", required=True, help="画布标题")
    parser.add_argument("--nodes", help="节点 JSON")
    parser.add_argument("--edges", help="边 JSON")
    args = parser.parse_args()
    
    nodes = json.loads(args.nodes) if args.nodes else []
    edges = json.loads(args.edges) if args.edges else []
    
    filename, filepath = create_canvas(args.vault, args.title, nodes, edges)
    
    print(f"Created: {filename}")
    print(f"Path: {filepath}")

if __name__ == "__main__":
    main()
