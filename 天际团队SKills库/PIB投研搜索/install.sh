#!/bin/bash
REPO="FutureX-Skills/futurex-skills"
SKILL="PIB投研搜索"
TARGET="$HOME/.agents/skills/$SKILL"
mkdir -p "$TARGET"
curl -fsSL "https://raw.githubusercontent.com/$REPO/main/$SKILL/SKILL.md" -o "$TARGET/SKILL.md"
curl -fsSL "https://raw.githubusercontent.com/$REPO/main/$SKILL/README.md" -o "$TARGET/README.md"
curl -fsSL "https://raw.githubusercontent.com/$REPO/main/$SKILL/ByteDance_PIB_Memo.txt" -o "$TARGET/ByteDance_PIB_Memo.txt" 2>/dev/null
mkdir -p "$TARGET/scripts"
curl -fsSL "https://raw.githubusercontent.com/$REPO/main/$SKILL/scripts/pib-search.py" -o "$TARGET/scripts/pib-search.py" 2>/dev/null
curl -fsSL "https://raw.githubusercontent.com/$REPO/main/$SKILL/scripts/pib-search.sh" -o "$TARGET/scripts/pib-search.sh" 2>/dev/null
curl -fsSL "https://raw.githubusercontent.com/$REPO/main/$SKILL/scripts/vc-memo.py" -o "$TARGET/scripts/vc-memo.py" 2>/dev/null
echo "✅ $SKILL 安装完成 → $TARGET"
