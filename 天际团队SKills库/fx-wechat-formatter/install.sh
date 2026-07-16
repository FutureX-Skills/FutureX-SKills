#!/bin/bash
set -e

REPO_PATH="天际团队SKills库/fx-wechat-formatter"
TARGET="${AGENTS_DIR:-$HOME/.agents/skills}/fx-wechat-formatter"
BASE_URL="https://raw.githubusercontent.com/FutureX-Skills/FutureX-SKills/main"

mkdir -p "$TARGET/scripts"
curl -fsSL "$BASE_URL/$REPO_PATH/SKILL.md" -o "$TARGET/SKILL.md"
curl -fsSL "$BASE_URL/$REPO_PATH/README.md" -o "$TARGET/README.md"
curl -fsSL "$BASE_URL/$REPO_PATH/scripts/build_docx.js" -o "$TARGET/scripts/build_docx.js"
echo "✅ fx-wechat-formatter 安装完成 → $TARGET"
