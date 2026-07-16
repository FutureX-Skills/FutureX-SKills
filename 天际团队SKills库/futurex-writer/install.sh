#!/bin/bash
set -e

REPO_PATH="天际团队SKills库/futurex-writer"
TARGET="${AGENTS_DIR:-$HOME/.agents/skills}/futurex-writer"
BASE_URL="https://raw.githubusercontent.com/FutureX-Skills/FutureX-SKills/main"

mkdir -p "$TARGET"
curl -fsSL "$BASE_URL/$REPO_PATH/SKILL.md" -o "$TARGET/SKILL.md"
curl -fsSL "$BASE_URL/$REPO_PATH/README.md" -o "$TARGET/README.md"
echo "✅ futurex-writer 安装完成 → $TARGET"
