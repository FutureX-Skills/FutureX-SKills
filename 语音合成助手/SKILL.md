# Text-to-Speech Skill

## Overview

This skill enables conversion of text into natural-sounding speech via the inference.sh CLI platform. It provides multiple TTS models optimized for different use cases.


## Quick Start

First, ensure the inference.sh CLI is installed:
```bash
npx skills add inference-sh/skills@agent-tools
```

Then authenticate and generate speech:
```bash
infsh login
infsh app run infsh/kokoro-tts --input '{"text": "Hello, welcome to our product demo."}'
```

## Available Models

| Model | App ID | Best For |
|-------|--------|----------|
| DIA TTS | `infsh/dia-tts` | Conversational, expressive voices |
| Kokoro TTS | `infsh/kokoro-tts` | Fast, natural output |
| Chatterbox | `infsh/chatterbox` | General-purpose applications |
| Higgs Audio | `infsh/higgs-audio` | Emotional control and expression |
| VibeVoice | `infsh/vibevoice` | Podcasts, long-form content |

## Usage Examples

**Basic speech generation:**
```bash
infsh app run infsh/kokoro-tts --input '{"text": "Welcome to our tutorial."}'
```

**Conversational TTS:**
```bash
infsh app sample infsh/dia-tts --save input.json
# Edit input.json with voice parameters
infsh app run infsh/dia-tts --input input.json
```

**Expressive speech with emotion:**
```bash
infsh app run infsh/higgs-audio --input '{"text": "This is incredible!", "emotion": "excited"}'
```

## Use Cases

- Product demos and explainer videos
- Audiobook narration
- Podcast episode generation
- Content accessibility
- IVR phone system prompts
- Video narration

## Integration with Video

Generate audio, then create talking-head videos using OmniHuman:
```bash
infsh app run infsh/kokoro-tts --input '{"text": "Your script"}' > speech.json
infsh app run bytedance/omnihuman-1-5 --input '{"image_url": "portrait.jpg", "audio_url": "<url>"}'
```

