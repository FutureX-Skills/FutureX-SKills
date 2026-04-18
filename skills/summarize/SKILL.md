---
name: summarize
description: Summarize URLs or files with the summarize CLI (web, PDFs, images, audio, YouTube).
homepage: https://summarize.sh
metadata: {"clawdbot":{"emoji":"🧾","requires":{"bins":["summarize"]},"install":[{"id":"brew","kind":"brew","formula":"steipete/tap/summarize","bins":["summarize"],"label":"Install summarize (brew)"}]}}
---

# 一键安装

```bash
# macOS
brew install steipete/tap/summarize

# 克隆仓库
git clone https://github.com/FutureX-Skills/FutureX-SKills.git ~/.openclaw/workspace/skills/summarize
```

> **前提条件**：已安装 summarize CLI，以及 API Key（OpenAI/Anthropic/xAI/Google 之一）

---

# Summarize

## 详细介绍

通用内容摘要工具，支持 URL、文件（PDF、图片）、音频和 YouTube 视频的摘要生成。

### 核心能力

- **URL 摘要**：网页内容快速提取和摘要
- **PDF 摘要**：处理扫描版和文本版 PDF
- **图片摘要**：图片内容识别和描述
- **音频摘要**：音频/视频转录和摘要（YouTube）
- **多模型支持**：OpenAI、Anthropic、xAI、Google Gemini

### 适用场景

```bash
# 摘要网页
summarize "https://example.com" --model google/gemini-3-flash-preview

# 摘要 PDF
summarize "/path/to/file.pdf" --model google/gemini-3-flash-preview

# 摘要 YouTube 视频
summarize "https://youtu.be/dQw4w9WgXcQ" --youtube auto

# 指定长度
summarize "https://example.com" --length long
```

### 参数说明

| 参数 | 说明 |
|------|------|
| `--length` | 输出长度：short/medium/long/xl/xxl/\<chars\> |
| `--model` | 使用的模型，默认 google/gemini-3-flash-preview |
| `--extract-only` | 仅提取 URL 内容，不摘要 |
| `--json` | JSON 格式输出 |
| `--youtube auto` | YouTube 自动转录 |

Fast CLI to summarize URLs, local files, and YouTube links.

## Quick start

```bash
summarize "https://example.com" --model google/gemini-3-flash-preview
summarize "/path/to/file.pdf" --model google/gemini-3-flash-preview
summarize "https://youtu.be/dQw4w9WgXcQ" --youtube auto
```

## Model + keys

Set the API key for your chosen provider:
- OpenAI: `OPENAI_API_KEY`
- Anthropic: `ANTHROPIC_API_KEY`
- xAI: `XAI_API_KEY`
- Google: `GEMINI_API_KEY` (aliases: `GOOGLE_GENERATIVE_AI_API_KEY`, `GOOGLE_API_KEY`)

Default model is `google/gemini-3-flash-preview` if none is set.

## Useful flags

- `--length short|medium|long|xl|xxl|<chars>`
- `--max-output-tokens <count>`
- `--extract-only` (URLs only)
- `--json` (machine readable)
- `--firecrawl auto|off|always` (fallback extraction)
- `--youtube auto` (Apify fallback if `APIFY_API_TOKEN` set)

## Config

Optional config file: `~/.summarize/config.json`

```json
{ "model": "openai/gpt-5.2" }
```

Optional services:
- `FIRECRAWL_API_KEY` for blocked sites
- `APIFY_API_TOKEN` for YouTube fallback
