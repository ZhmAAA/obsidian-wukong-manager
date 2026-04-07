#!/usr/bin/env python3
"""清理 Obsidian Vault 中的临时文件"""
import os
import shutil
import argparse

def cleanup_vault(vault_path, dry_run=True):
    """清理 vault 中的临时文件"""
    patterns = [
        ".obsidian/workspace.json.bak",
        ".obsidian/workspace.json",
        "tmp/",
        ".trash/",
    ]
    
    removed = []
    
    for root, dirs, files in os.walk(vault_path):
        for d in dirs:
            if d in ["tmp", ".trash", "__pycache__"]:
                path = os.path.join(root, d)
                removed.append(path)
                if not dry_run:
                    shutil.rmtree(path)
        
        for f in files:
            if f.endswith((".bak", ".tmp", ".swp")):
                path = os.path.join(root, f)
                removed.append(path)
                if not dry_run:
                    os.remove(path)
    
    return removed

def main():
    parser = argparse.ArgumentParser(description="清理 Obsidian Vault")
    parser.add_argument("--vault", required=True, help="Vault 路径")
    parser.add_argument("--execute", action="store_true", help="实际执行清理（默认 dry-run）")
    args = parser.parse_args()
    
    removed = cleanup_vault(args.vault, dry_run=not args.execute)
    
    if removed:
        print(f"将删除 {len(removed)} 个项目:")
        for item in removed:
            print(f"  - {item}")
        if not args.execute:
            print("\n使用 --execute 确认执行清理")
    else:
        print("没有需要清理的项目")

if __name__ == "__main__":
    main()
