---
name: obsidian-wukong-manager
description: Obsidian note vault manager for Markdown notes, Canvas diagrams, and database views. Use when user needs: (1) Create Obsidian notes or knowledge base (2) Generate mind maps/knowledge graphs (3) Manage project databases/kanban boards (4) Handle wikilinks/tags/Front Matter. Supports double brackets, hash tags, callout syntax.
---

# Obsidian-WuKongManager

Obsidian vault management skill, converted from official Obsidian Skills, provides native Obsidian operations for Wukong.

## Core Features

### 1. Markdown Note Management

**Syntax:**
- Wikilinks: [[Note Title]], [[Note|Display Text]]
- Embed: ![[Note Title]]
- Tags: #tag, #category/subtag
- Callouts: > [!note] Content

**Front Matter Template:**
```yaml
---
title: {Title}
created: {YYYY-MM-DD HH:MM}
tags: [{tag1}, {tag2}]
aliases: [{alias}]
---

{Body}
```

### 2. Canvas Operations

Create mind maps, knowledge graphs, flowcharts. Node types: text, file, link, group.

**Node Structure:**
```json
{
  "id": "unique-id",
  "type": "text",
  "text": "Content",
  "x": 0, "y": 0,
  "width": 200, "height": 100,
  "color": "blue"
}
```

**Colors:** blue, green, yellow, orange, red, purple, gray, pink

### 3. Database Views

Three view types:
- **Table View**: Dataview format Markdown tables
- **Index View**: YAML + Dataview queries
- **Kanban View**: Markdown todo list groups

## Workflow

1. Confirm Vault path
2. Parse user intent
3. Execute generation using scripts
4. Deliver with deliver_artifacts

## Scripts

- create_note.py: Create Markdown notes
- create_canvas.py: Create Canvas diagrams  
- create_database.py: Create database views

See references/obsidian-syntax.md for detailed syntax.
