---
name: tavily
description: AI-optimized web search via Tavily API. Returns concise, relevant results for AI agents.
homepage: https://tavily.com
metadata: {"clawdbot":{"emoji":"🔍","requires":{"bins":["node"],"env":["TAVILY_API_KEY"]},"primaryEnv":"TAVILY_API_KEY"}}
---

# 一键安装

```bash
# 克隆仓库
git clone https://github.com/FutureX-Skills/FutureX-SKills.git ~/.openclaw/workspace/skills/tavily-search

# 获取 API Key
# 1. 访问 https://app.tavily.com
# 2. 注册并获取 API Key
# 3. 设置环境变量
export TAVILY_API_KEY="tvly-xxx"
```

> **前提条件**：Node.js 和 Tavily API Key（免费注册有额度限制）

---

# Tavily Search

## 详细介绍

AI 优化的网页搜索工具，专为 AI Agent 设计，返回简洁、相关的搜索结果。比传统搜索引擎更适合 AI 处理。

### 核心能力

- **AI 优化搜索**：返回干净、结构化的搜索结果
- **深度搜索模式**：使用 `--deep` 获取更全面的结果
- **新闻搜索**：支持新闻话题搜索（`--topic news`）
- **URL 内容提取**：从特定 URL 提取内容

### 适用场景

```bash
# 基础搜索
node scripts/search.mjs "AI 最新发展"

# 返回 10 条结果
node scripts/search.mjs "AI 最新发展" -n 10

# 深度搜索
node scripts/search.mjs "AI 最新发展" --deep

# 新闻话题
node scripts/search.mjs "AI 最新发展" --topic news

# 从 URL 提取内容
node scripts/extract.mjs "https://example.com/article"
```

### 注意事项

- 需要 Tavily API Key（https://tavily.com 免费注册）
- 默认返回 5 条结果，最大 20 条
- `--topic news` 限制结果为最近发布的内容
