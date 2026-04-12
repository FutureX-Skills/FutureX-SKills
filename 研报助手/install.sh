#!/bin/bash
# 研报助手 - FutureX Capital 多智能体调度中心
# 使用方式：
#   git clone https://github.com/FutureX-Skills/futurex-skills.git
#   cd futurex-skills/研报助手
#   bash install.sh
#
# 或一行命令：
#   git clone --depth=1 https://github.com/FutureX-Skills/futurex-skills.git /tmp/fx-skills && cp -r /tmp/fx-skills/研报助手 ~/.agents/skills/ && rm -rf /tmp/fx-skills

echo "研报助手安装中..."
TARGET_DIR="$HOME/.agents/skills/研报助手"
git clone --depth=1 https://github.com/FutureX-Skills/futurex-skills.git /tmp/fx-skills-tmp
mkdir -p "$TARGET_DIR"
cp -r /tmp/fx-skills-tmp/研报助手/* "$TARGET_DIR/"
rm -rf /tmp/fx-skills-tmp
echo "研报助手安装完成 → $TARGET_DIR"
