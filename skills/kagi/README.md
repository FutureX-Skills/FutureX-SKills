# 一键安装

```bash
# 克隆仓库
git clone https://github.com/FutureX-Skills/FutureX-SKills.git ~/.openclaw/workspace/skills/kagi

# 获取 Kagi API Key
# 1. 访问 https://kagi.com/settings/api
# 2. 创建 API Token
# 3. 设置环境变量
export KAGI_API_TOKEN='your-token-here'
```

> **前提条件**：Kagi API Token（https://kagi.com 免费注册有额度限制）

---

# kagi-skill

OpenClaw skill: Kagi API (Search + FastGPT)

## What’s here

- `SKILL.md` — skill metadata + usage notes
- `scripts/` — tiny Python (no deps) wrappers for Kagi API
- `references/` — quick API/auth notes

## Setup

Create a Kagi API token: https://kagi.com/settings/api

Make it available to the scripts:

```bash
export KAGI_API_TOKEN='...'
```

## Usage

```bash
python3 scripts/kagi_search.py "steve jobs" --limit 5
python3 scripts/kagi_fastgpt.py "Summarize Python 3.11" 
```
