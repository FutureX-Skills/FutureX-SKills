#!/bin/bash
REPO="FutureX-Skills/futurex-skills"
SKILL="LinkedIn内容助手"
TARGET="$HOME/.agents/skills/$SKILL"
mkdir -p "$TARGET"
curl -fsSL "https://raw.githubusercontent.com/$REPO/main/$SKILL/SKILL.md" -o "$TARGET/SKILL.md"
curl -fsSL "https://raw.githubusercontent.com/$REPO/main/$SKILL/linkedin-short-post-SKILL.md" -o "$TARGET/linkedin-short-post-SKILL.md"
curl -fsSL "https://raw.githubusercontent.com/$REPO/main/$SKILL/linkedin-long-post-SKILL.md" -o "$TARGET/linkedin-long-post-SKILL.md"
echo "✅ LinkedIn内容助手（短帖子+长文章）安装完成 → $TARGET"
