#!/bin/bash
REPO="FutureX-Skills/futurex-skills"
SKILL="金融网页构建器"
TARGET="$HOME/.agents/skills/$SKILL"
mkdir -p "$TARGET"
curl -fsSL "https://raw.githubusercontent.com/$REPO/main/$SKILL/SKILL.md" -o "$TARGET/SKILL.md"
curl -fsSL "https://raw.githubusercontent.com/$REPO/main/$SKILL/README.md" -o "$TARGET/README.md"
# 脚本需单独下载
curl -fsSL "https://raw.githubusercontent.com/$REPO/main/$SKILL/scripts/bundle-artifact.sh" -o "$TARGET/scripts/bundle-artifact.sh" 2>/dev/null
curl -fsSL "https://raw.githubusercontent.com/$REPO/main/$SKILL/scripts/init-artifact.sh" -o "$TARGET/scripts/init-artifact.sh" 2>/dev/null
echo "✅ $SKILL 安装完成 → $TARGET"
