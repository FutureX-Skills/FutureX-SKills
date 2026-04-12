#!/bin/bash
# FutureX Skills 全量安装脚本
# 运行此脚本将安装天际团队全部 Skills 到 ~/.agents/skills/

REPO="FutureX-Skills/futurex-skills"
TARGET="$HOME/.agents/skills"

echo "📦 FutureX Skills 全量安装中..."
echo "目标目录: $TARGET"
echo ""

# 安装天际团队SKills库
echo "📂 安装天际团队SKills库..."
git clone --depth=1 https://github.com/$REPO.git /tmp/fx-skills-tmp
for dir in /tmp/fx-skills-tmp/天际团队SKills库/*/; do
  skill=$(basename "$dir")
  echo "  ✅ 安装 $skill"
  mkdir -p "$TARGET/$skill"
  cp -r "$dir"*.md "$TARGET/$skill/" 2>/dev/null
  cp -r "$dir"scripts "$TARGET/$skill/" 2>/dev/null
done

# 安装外部精选Skills
echo ""
echo "📂 安装外部精选Skills..."
for dir in /tmp/fx-skills-tmp/外部精选Skills/*/; do
  skill=$(basename "$dir")
  echo "  ✅ 安装 $skill"
  mkdir -p "$TARGET/$skill"
  cp -r "$dir"*.md "$TARGET/$skill/" 2>/dev/null
  cp -r "$dir"scripts "$TARGET/$skill/" 2>/dev/null
done

rm -rf /tmp/fx-skills-tmp
echo ""
echo "✅ 安装完成！共安装 $(ls $TARGET | wc -l) 个 Skills"
echo "查看所有Skills: ls ~/.agents/skills/"
