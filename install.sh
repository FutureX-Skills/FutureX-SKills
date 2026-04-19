#!/bin/bash
# FutureX Skills 一键安装全部 Skills 脚本
# Usage: curl -fsSL https://raw.githubusercontent.com/FutureX-Skills/FutureX-SKills/main/install.sh | bash

AGENTS_DIR="${AGENTS_DIR:-$HOME/.claude/skills}"

install_from_path() {
    local REPO_PATH="$1"    # e.g. "天际团队SKills库/研报助手"
    local SKILL_NAME="$2"   # e.g. "研报助手"
    local TARGET="$AGENTS_DIR/$SKILL_NAME"
    
    if [ -d "$TARGET" ]; then
        echo "⏭  $SKILL_NAME 已安装，跳过"
        return 0
    fi
    
    mkdir -p "$TARGET"
    curl -fsSL "https://raw.githubusercontent.com/FutureX-Skills/FutureX-SKills/main/$REPO_PATH/SKILL.md" -o "$TARGET/SKILL.md" 2>/dev/null
    curl -fsSL "https://raw.githubusercontent.com/FutureX-Skills/FutureX-SKills/main/$REPO_PATH/README.md" -o "$TARGET/README.md" 2>/dev/null
    
    if [ -f "$TARGET/SKILL.md" ]; then
        echo "✅ $SKILL_NAME 安装完成"
        return 0
    else
        echo "❌ $SKILL_NAME 安装失败"
        rm -rf "$TARGET"
        return 1
    fi
}

echo "📦 安装天际团队 Skills..."
for skill in "AI-VC推文助手" "AI内容写作助手" "LinkedIn内容助手" "PE募资追踪器" "PIB投研搜索" "TODO任务追踪" "VC创始人会面准备" "事项提醒" "云Token监控" "会议纪要整理助手" "公众号排版助手" "多媒体处理助手" "小红书自动发布" "投资-Memo" "播客后期助手" "旅行规划助手" "研报助手" "硅谷季度报告" "社媒内容处理" "社媒营销" "立项报告" "视频标题大师" "语音合成助手" "费用报销合规检查" "金融网页构建器" "项目立项投资报告"; do
    install_from_path "天际团队SKills库/$skill" "$skill"
done

echo ""
echo "📦 安装 43-Agent-skills..."
for skill in "chat-archiver" "email-invoice-processor" "feishu-assistant" "find-skills" "follow-builders" "media-transcriber" "social-media-scout" "video-creator" "web-browser"; do
    install_from_path "外部精选Skills/43-Agent-skills/$skill" "$skill"
done

echo ""
echo "📦 安装李继刚skills..."
for skill in "ljg-card" "ljg-invest" "ljg-learn" "ljg-paper-flow" "ljg-paper-river" "ljg-paper" "ljg-plain" "ljg-rank" "ljg-relationship" "ljg-roundtable" "ljg-skill-map" "ljg-think" "ljg-travel" "ljg-word-flow" "ljg-word" "ljg-writes"; do
    install_from_path "外部精选Skills/李继刚skills/$skill" "$skill"
done

echo ""
echo "📦 安装其他外部精选Skills..."
for skill in "skill-creator" "qiaomu-markdown-proxy" "Skill-Vetter"; do
    install_from_path "外部精选Skills/$skill" "$skill"
done

echo ""
echo "🎉 全部安装完成！"
