---
name: openai-whisper
description: Local speech-to-text with the Whisper CLI (no API key).
homepage: https://openai.com/research/whisper
metadata: {"clawdbot":{"emoji":"🎙️","requires":{"bins":["whisper"]},"install":[{"id":"brew","kind":"brew","formula":"openai-whisper","bins":["whisper"],"label":"Install OpenAI Whisper (brew)"}]}}
---

# 一键安装

```bash
# macOS
brew install openai-whisper

# 克隆仓库
git clone https://github.com/FutureX-Skills/FutureX-SKills.git ~/.openclaw/workspace/skills/openai-whisper
```

> **前提条件**：已安装 Whisper CLI（首次使用会自动下载模型到 ~/.cache/whisper）

---

# Whisper (CLI)

## 详细介绍

OpenAI Whisper 本地语音转文字工具，无需 API Key，完全本地运行。支持多种语言和音频格式。

### 核心能力

- **本地转录**：无需网络，完全离线运行
- **无需 API Key**：完全免费
- **多语言支持**：支持中文、英文等多种语言
- **多格式支持**：MP3、M4A、WAV 等常见音频格式
- **翻译功能**：支持将音频翻译为英文

### 适用场景

| 任务 | 命令 |
|------|------|
| 转录为文本 | `whisper /path/audio.mp3 --model medium --output_format txt` |
| 翻译为英文 | `whisper /path/audio.m4a --task translate --output_format srt` |
| 指定输出格式 | `whisper audio.mp3 --output_format json --output_dir ./results` |

### 模型选择

| 模型 | 速度 | 准确性 | 首次使用 |
|------|------|--------|---------|
| tiny | 最快 | 较低 | ~75MB |
| base | 快 | 中等 | ~75MB |
| small | 中等 | 较高 | ~465MB |
| medium | 较慢 | 高 | ~1.5GB |
| turbo | 快 | 高 | 默认模型 |

### 注意事项

- 模型文件首次运行时自动下载到 `~/.cache/whisper`
- `--model` 默认为 `turbo`

Use `whisper` to transcribe audio locally.

Quick start
- `whisper /path/audio.mp3 --model medium --output_format txt --output_dir .`
- `whisper /path/audio.m4a --task translate --output_format srt`

Notes
- Models download to `~/.cache/whisper` on first run.
- `--model` defaults to `turbo` on this install.
- Use smaller models for speed, larger for accuracy.
