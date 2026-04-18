---
name: gog
description: Google Workspace CLI for Gmail, Calendar, Drive, Contacts, Sheets, and Docs.
homepage: https://gogcli.sh
metadata: {"clawdbot":{"emoji":"🎮","requires":{"bins":["gog"]},"install":[{"id":"brew","kind":"brew","formula":"steipete/tap/gogcli","bins":["gog"],"label":"Install gog (brew)"}]}}
---

# 一键安装

```bash
# macOS
brew install steipete/tap/gogcli

# 克隆仓库
git clone https://github.com/FutureX-Skills/FutureX-SKills.git ~/.openclaw/workspace/skills/gog
```

> **前提条件**：已安装 gog CLI，并完成 Google OAuth 认证。

---

# gog

## 详细介绍

Google Workspace 全套 CLI 工具，通过命令行管理 Gmail、Google Calendar、Google Drive、Google Contacts、Google Sheets 和 Google Docs。

### 核心能力

- **Gmail**：搜索邮件、发送邮件、管理标签
- **Calendar**：查看和创建日历事件
- **Drive**：搜索文件、管理文件夹
- **Contacts**：查看和管理联系人
- **Sheets**：读取、更新、追加表格数据
- **Docs**：导出文档内容

### 适用场景

| 任务 | 命令示例 |
|------|---------|
| 搜索邮件 | `gog gmail search 'newer_than:7d' --max 10` |
| 发送邮件 | `gog gmail send --to a@b.com --subject "Hi" --body "Hello"` |
| 查看日历 | `gog calendar events <calendarId> --from <iso> --to <iso>` |
| 搜索文件 | `gog drive search "query" --max 10` |
| 读取表格 | `gog sheets get <sheetId> "Tab!A1:D10" --json` |
| 导出文档 | `gog docs export <docId> --format txt --out /tmp/doc.txt` |

### 初始配置

```bash
# 配置凭证
gog auth credentials /path/to/client_secret.json

# 添加账户
gog auth add you@gmail.com --services gmail,calendar,drive,contacts,sheets,docs

# 查看已配置账户
gog auth list
```

Use `gog` for Gmail/Calendar/Drive/Contacts/Sheets/Docs. Requires OAuth setup.

Setup (once)
- `gog auth credentials /path/to/client_secret.json`
- `gog auth add you@gmail.com --services gmail,calendar,drive,contacts,sheets,docs`
- `gog auth list`

Common commands
- Gmail search: `gog gmail search 'newer_than:7d' --max 10`
- Gmail send: `gog gmail send --to a@b.com --subject "Hi" --body "Hello"`
- Calendar: `gog calendar events <calendarId> --from <iso> --to <iso>`
- Drive search: `gog drive search "query" --max 10`
- Contacts: `gog contacts list --max 20`
- Sheets get: `gog sheets get <sheetId> "Tab!A1:D10" --json`
- Sheets update: `gog sheets update <sheetId> "Tab!A1:B2" --values-json '[["A","B"],["1","2"]]' --input USER_ENTERED`
- Sheets append: `gog sheets append <sheetId> "Tab!A:C" --values-json '[["x","y","z"]]' --insert INSERT_ROWS`
- Sheets clear: `gog sheets clear <sheetId> "Tab!A2:Z"`
- Sheets metadata: `gog sheets metadata <sheetId> --json`
- Docs export: `gog docs export <docId> --format txt --out /tmp/doc.txt`
- Docs cat: `gog docs cat <docId>`

Notes
- Set `GOG_ACCOUNT=you@gmail.com` to avoid repeating `--account`.
- For scripting, prefer `--json` plus `--no-input`.
- Sheets values can be passed via `--values-json` (recommended) or as inline rows.
- Docs supports export/cat/copy. In-place edits require a Docs API client (not in gog).
- Confirm before sending mail or creating events.
