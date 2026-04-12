#!/bin/bash
REPO="FutureX-Skills/futurex-skills"
SKILL="项目立项投资报告"
TARGET="$HOME/.agents/skills/$SKILL"
mkdir -p "$TARGET"
curl -fsSL "https://raw.githubusercontent.com/$REPO/main/$SKILL/SKILL.md" -o "$TARGET/SKILL.md"
curl -fsSL "https://raw.githubusercontent.com/$REPO/main/$SKILL/README.md" -o "$TARGET/README.md"
echo "✅ $SKILL 安装完成 → $TARGET"
