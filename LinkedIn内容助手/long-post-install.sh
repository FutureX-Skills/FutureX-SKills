#!/bin/bash
REPO="FutureX-Skills/futurex-skills"
SKILL="LinkedIn内容助手"
TARGET="$HOME/.agents/skills/$SKILL"
mkdir -p "$TARGET"
curl -fsSL "https://raw.githubusercontent.com/$REPO/main/$SKILL/linkedin-long-post-SKILL.md" -o "$TARGET/linkedin-long-post-SKILL.md"
echo "✅ LinkedIn长文章 skill 安装完成"
