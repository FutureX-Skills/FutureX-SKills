#!/bin/bash
REPO="FutureX-Skills/futurex-skills"
SKILL="LinkedIn内容助手"
TARGET="$HOME/.agents/skills/$SKILL"
mkdir -p "$TARGET"
curl -fsSL "https://raw.githubusercontent.com/$REPO/main/$SKILL/linkedin-short-post-SKILL.md" -o "$TARGET/linkedin-short-post-SKILL.md"
echo "✅ LinkedIn短帖子 skill 安装完成"
