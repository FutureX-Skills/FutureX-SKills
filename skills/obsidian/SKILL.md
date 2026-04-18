---
name: obsidian
description: Work with Obsidian vaults (plain Markdown notes) and automate via obsidian-cli.
homepage: https://help.obsidian.md
metadata: {"clawdbot":{"emoji":"💎","requires":{"bins":["obsidian-cli"]},"install":[{"id":"brew","kind":"brew","formula":"yakitrak/yakitrak/obsidian-cli","bins":["obsidian-cli"],"label":"Install obsidian-cli (brew)"}]}}
---

# 一键安装

```bash
# macOS
brew install yakitrak/yakitrak/obsidian-cli

# 克隆仓库
git clone https://github.com/FutureX-Skills/FutureX-SKills.git ~/.openclaw/workspace/skills/obsidian
```

> **前提条件**：obsidian-cli，以及 Obsidian 桌面应用（用于读取 vault 配置）。

---

# Obsidian

## 详细介绍

Obsidian 笔记库管理工具，通过 obsidian-cli 操作 Obsidian vault 中的笔记文件。Vault 本质上是磁盘上的普通文件夹。

### 核心能力

- **查找 Vault**：从 Obsidian 配置中自动发现当前打开的 vault
- **搜索笔记**：按名称搜索、按内容搜索
- **创建笔记**：通过 CLI 创建新笔记
- **移动/重命名**：安全地移动笔记，自动更新所有 wikilinks
- **删除笔记**：通过 CLI 删除

### 适用场景

| 任务 | 命令 |
|------|------|
| 设置默认 vault | `obsidian-cli set-default "vault-name"` |
| 搜索笔记名 | `obsidian-cli search "query"` |
| 按内容搜索 | `obsidian-cli search-content "query"` |
| 创建笔记 | `obsidian-cli create "Folder/New note" --content "..."` |
| 移动/重命名 | `obsidian-cli move "old/path" "new/path"` |
| 删除笔记 | `obsidian-cli delete "path/note"` |

### Vault 结构

```
vault/
├── notes/*.md           # 纯文本 Markdown 文件
├── .obsidian/           # 工作区和插件配置
├── *.canvas             # Canvas 文件（JSON）
└── attachments/          # 附件文件夹
```

### 注意事项

- Obsidian 支持多 vault（iCloud vs 本地文档、工作/个人等）
- 不要硬编码 vault 路径，优先读取配置
- 通过 URI 创建笔记需要 Obsidian URI handler 正常工作

Obsidian vault = a normal folder on disk.

Vault structure (typical)
- Notes: `*.md` (plain text Markdown; edit with any editor)
- Config: `.obsidian/` (workspace + plugin settings; usually don’t touch from scripts)
- Canvases: `*.canvas` (JSON)
- Attachments: whatever folder you chose in Obsidian settings (images/PDFs/etc.)

## Find the active vault(s)

Obsidian desktop tracks vaults here (source of truth):
- `~/Library/Application Support/obsidian/obsidian.json`

`obsidian-cli` resolves vaults from that file; vault name is typically the **folder name** (path suffix).

Fast “what vault is active / where are the notes?”
- If you’ve already set a default: `obsidian-cli print-default --path-only`
- Otherwise, read `~/Library/Application Support/obsidian/obsidian.json` and use the vault entry with `"open": true`.

Notes
- Multiple vaults common (iCloud vs `~/Documents`, work/personal, etc.). Don’t guess; read config.
- Avoid writing hardcoded vault paths into scripts; prefer reading the config or using `print-default`.

## obsidian-cli quick start

Pick a default vault (once):
- `obsidian-cli set-default "<vault-folder-name>"`
- `obsidian-cli print-default` / `obsidian-cli print-default --path-only`

Search
- `obsidian-cli search "query"` (note names)
- `obsidian-cli search-content "query"` (inside notes; shows snippets + lines)

Create
- `obsidian-cli create "Folder/New note" --content "..." --open`
- Requires Obsidian URI handler (`obsidian://…`) working (Obsidian installed).
- Avoid creating notes under “hidden” dot-folders (e.g. `.something/...`) via URI; Obsidian may refuse.

Move/rename (safe refactor)
- `obsidian-cli move "old/path/note" "new/path/note"`
- Updates `[[wikilinks]]` and common Markdown links across the vault (this is the main win vs `mv`).

Delete
- `obsidian-cli delete "path/note"`

Prefer direct edits when appropriate: open the `.md` file and change it; Obsidian will pick it up.
