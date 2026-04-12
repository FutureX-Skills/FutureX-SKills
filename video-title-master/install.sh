#!/bin/bash
echo "视频封面标题大师安装中..."
TARGET_DIR="$HOME/.agents/skills/video-title-master"
git clone --depth=1 https://github.com/FutureX-Skills/futurex-skills.git /tmp/fx-skills-tmp
mkdir -p "$TARGET_DIR"
cp -r /tmp/fx-skills-tmp/video-title-master/* "$TARGET_DIR/"
rm -rf /tmp/fx-skills-tmp
echo "视频封面标题大师安装完成 → $TARGET_DIR"
