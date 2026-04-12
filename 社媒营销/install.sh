#!/bin/bash
echo "社媒营销 skill 安装中..."
TARGET_DIR="$HOME/.agents/skills/社媒营销"
git clone --depth=1 https://github.com/FutureX-Skills/futurex-skills.git /tmp/fx-skills-tmp
mkdir -p "$TARGET_DIR"
cp -r /tmp/fx-skills-tmp/社媒营销/* "$TARGET_DIR/"
rm -rf /tmp/fx-skills-tmp
echo "社媒营销安装完成 → $TARGET_DIR"
