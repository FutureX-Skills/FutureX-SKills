---
name: feishu-voice-setup
description: "One-command setup for Feishu voice I/O (TTS + STT). Configures Edge TTS with Chinese voice, enables audio transcription, and patches Feishu to send voice bubbles instead of file attachments. Run: python3 {SKILL_DIR}/scripts/setup.py"
author: "Clara"
user-invocable: true
metadata:
  { "openclaw": { "emoji": "🎙️", "requires": { "bins": ["python3", "ffmpeg"] } } }
---

# 一键安装

```bash
# 克隆仓库
git clone https://github.com/FutureX-Skills/FutureX-SKills.git ~/.openclaw/workspace/skills/feishu-voice-setup

# 运行一键设置
python3 {SKILL_DIR}/scripts/setup.py
```

> **前提条件**：Python3 + ffmpeg + OpenClaw >= 2026.3.x

---

# Feishu Voice I/O Setup

One-command onboarding for Feishu voice input/output on OpenClaw.

## What It Does

1. **Voice Output (TTS)**: Bot replies are sent as native Feishu voice bubbles using Edge TTS (free, unlimited)
2. **Voice Input (STT)**: Incoming voice messages are auto-transcribed
3. **Opus Conversion**: Patches Feishu plugin to auto-convert MP3→Opus (required for voice bubbles)

## Quick Setup

```bash
python3 {SKILL_DIR}/scripts/setup.py
```

This will:
- Check prerequisites (OpenClaw >= 2026.3.x, ffmpeg, edge-tts)
- Install `edge-tts` if missing
- Apply config changes to `~/.openclaw/openclaw.json`
- Patch Feishu `media.ts` for MP3→Opus auto-conversion
- Restart the gateway

## What Gets Configured

| Setting | Value | Purpose |
|---------|-------|---------|
| `tools.media.audio.enabled` | `true` | Auto-transcribe incoming voice messages |
| `messages.tts.auto` | `"inbound"` | Auto-reply with voice when user sends voice |
| `messages.tts.provider` | `"edge"` | Free Microsoft Edge TTS engine |
| `messages.tts.edge.voice` | `"zh-CN-YunxiNeural"` | Chinese male voice (Yunxi) |
| `messages.tts.edge.lang` | `"zh-CN"` | Chinese language |

## The Opus Patch (Why It's Needed)

Feishu only sends audio as voice bubbles when the file is `.opus` or `.ogg`. OpenClaw's built-in TTS generates `.mp3` files. Without this patch, voice replies arrive as file attachments instead of playable voice bubbles.

The patch adds an ffmpeg conversion step in the Feishu outbound adapter (`media.ts`) that transparently converts MP3→Opus before uploading.

**Note:** This patch is applied to `node_modules` and will be lost on `npm update openclaw`. Re-run setup after updating.

## Re-apply After OpenClaw Update

```bash
python3 {SKILL_DIR}/scripts/patch_media.py
openclaw gateway restart
```

## Change Voice

Edit `messages.tts.edge.voice` in `~/.openclaw/openclaw.json`:

```bash
# List available Chinese voices
edge-tts --list-voices | grep zh-CN
```

Common voices:
- `zh-CN-YunxiNeural` — Yunxi, lively male (default)
- `zh-CN-YunjianNeural` — Yunjian, passionate male
- `zh-CN-YunyangNeural` — Yunyang, professional male
- `zh-CN-XiaoxiaoNeural` — Xiaoxiao, gentle female
- `zh-CN-XiaoyiNeural` — Xiaoyi, lively female

## TTS Auto Modes

Edit `messages.tts.auto` in config:
- `"inbound"` — Voice reply only when user sends voice (default, recommended)
- `"always"` — Voice reply to every message (can cause duplicates)
- `"tagged"` — Only when agent uses `[[tts]]` tag
- `"off"` — Disable auto TTS

## Dependencies

- **ffmpeg** — Audio format conversion (install: `brew install ffmpeg`)
- **edge-tts** — Microsoft Edge TTS (install: `pip install edge-tts`)
- **OpenClaw >= 2026.3.x** — Voice support requires this version
