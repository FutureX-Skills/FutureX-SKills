#!/bin/bash
# 外部精选Skills 安装脚本
# 运行此脚本将所有精选 skill 复制到 ~/.agents/skills/
REPO="FutureX-Skills/futurex-skills"
TARGET="$HOME/.agents/skills"
SKILLS_DIR="$TARGET/外部精选Skills"
mkdir -p "$TARGET"
# Clone 并复制所有 skill
git clone --depth=1 https://github.com/FutureX-Skills/futurex-skills.git /tmp/fx-skills-tmp
cp -r /tmp/fx-skills-tmp/外部精选Skills/* "$TARGET/"
rm -rf /tmp/fx-skills-tmp
echo "✅ 外部精选Skills 安装完成 → $SKILLS_DIR"
