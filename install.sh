#!/bin/bash
# FutureX Skills 一键安装脚本
# Usage: curl -fsSL https://raw.githubusercontent.com/FutureX-Skills/FutureX-SKills/main/install.sh | bash
# Install one Skill: curl -fsSL .../install.sh | bash -s -- <skill-id>

set -u
AGENTS_DIR="${AGENTS_DIR:-$HOME/.agents/skills}"
ONLY_SKILL="${1:-}"
RAW_BASE="https://raw.githubusercontent.com/FutureX-Skills/FutureX-SKills/main"

install_from_path() {
    local REPO_PATH="$1"
    local SKILL_NAME="$2"
    if [ -n "$ONLY_SKILL" ] && [ "$ONLY_SKILL" != "$SKILL_NAME" ]; then return 0; fi
    local TARGET="$AGENTS_DIR/$SKILL_NAME"
    local SKILL_SOURCE="$REPO_PATH/SKILL.md"
    if [[ "$REPO_PATH" == *.md ]]; then SKILL_SOURCE="$REPO_PATH"; fi

    if [ -f "$TARGET/SKILL.md" ]; then
        echo "⏭  $SKILL_NAME 已安装，跳过"
        return 0
    fi

    mkdir -p "$TARGET"
    if ! curl -fsSL "$RAW_BASE/$SKILL_SOURCE" -o "$TARGET/SKILL.md"; then
        echo "❌ $SKILL_NAME 安装失败"
        rm -rf "$TARGET"
        return 1
    fi
    if [[ "$REPO_PATH" != *.md ]]; then
        curl -fsSL "$RAW_BASE/$REPO_PATH/README.md" -o "$TARGET/README.md" 2>/dev/null || true
    fi
    echo "✅ $SKILL_NAME 安装完成"
}

# CATALOG:START
echo "📦 安装 FutureX Skills（${ONLY_SKILL:-全部}）..."
install_from_path "天际团队SKills库/研报助手" "研报助手"
install_from_path "天际团队SKills库/PIB投研搜索" "PIB投研搜索"
install_from_path "天际团队SKills库/投资-Memo" "投资-Memo"
install_from_path "天际团队SKills库/立项报告" "立项报告"
install_from_path "天际团队SKills库/项目立项投资报告" "项目立项投资报告"
install_from_path "天际团队SKills库/硅谷季度报告" "硅谷季度报告"
install_from_path "天际团队SKills库/PE募资追踪器" "PE募资追踪器"
install_from_path "天际团队SKills库/vcpe-fundraising-tracker" "vcpe-fundraising-tracker"
install_from_path "天际团队SKills库/视频标题大师" "视频标题大师"
install_from_path "天际团队SKills库/AI内容写作助手" "AI内容写作助手"
install_from_path "天际团队SKills库/futurex-writer" "futurex-writer"
install_from_path "天际团队SKills库/公众号排版助手" "公众号排版助手"
install_from_path "天际团队SKills库/fx-wechat-formatter" "fx-wechat-formatter"
install_from_path "天际团队SKills库/AI-VC推文助手" "AI-VC推文助手"
install_from_path "天际团队SKills库/LinkedIn内容助手" "LinkedIn内容助手"
install_from_path "天际团队SKills库/播客后期助手" "播客后期助手"
install_from_path "天际团队SKills库/旅行规划助手" "旅行规划助手"
install_from_path "天际团队SKills库/金融网页构建器" "金融网页构建器"
install_from_path "天际团队SKills库/社媒营销" "社媒营销"
install_from_path "天际团队SKills库/社媒内容处理" "社媒内容处理"
install_from_path "天际团队SKills库/小红书自动发布" "小红书自动发布"
install_from_path "天际团队SKills库/语音合成助手" "语音合成助手"
install_from_path "天际团队SKills库/多媒体处理助手" "多媒体处理助手"
install_from_path "天际团队SKills库/会议纪要整理助手" "会议纪要整理助手"
install_from_path "天际团队SKills库/VC创始人会面准备" "VC创始人会面准备"
install_from_path "天际团队SKills库/云Token监控" "云Token监控"
install_from_path "天际团队SKills库/费用报销合规检查" "费用报销合规检查"
install_from_path "天际团队SKills库/pptx-logo-label-fix" "pptx-logo-label-fix"
install_from_path "天际团队SKills库/sg-luma-events" "sg-luma-events"
install_from_path "外部精选Skills/李继刚skills/ljg-invest" "ljg-invest"
install_from_path "外部精选Skills/李继刚skills/ljg-learn" "ljg-learn"
install_from_path "外部精选Skills/李继刚skills/ljg-paper" "ljg-paper"
install_from_path "外部精选Skills/李继刚skills/ljg-paper-river" "ljg-paper-river"
install_from_path "外部精选Skills/李继刚skills/ljg-plain" "ljg-plain"
install_from_path "外部精选Skills/李继刚skills/ljg-rank" "ljg-rank"
install_from_path "外部精选Skills/李继刚skills/ljg-relationship" "ljg-relationship"
install_from_path "外部精选Skills/李继刚skills/ljg-roundtable" "ljg-roundtable"
install_from_path "外部精选Skills/李继刚skills/ljg-think" "ljg-think"
install_from_path "外部精选Skills/李继刚skills/ljg-travel" "ljg-travel"
install_from_path "外部精选Skills/李继刚skills/ljg-word" "ljg-word"
install_from_path "外部精选Skills/李继刚skills/ljg-writes" "ljg-writes"
install_from_path "外部精选Skills/李继刚skills/ljg-card" "ljg-card"
install_from_path "外部精选Skills/43-Agent-skills/chat-archiver" "chat-archiver"
install_from_path "外部精选Skills/43-Agent-skills/feishu-assistant" "feishu-assistant"
install_from_path "外部精选Skills/43-Agent-skills/follow-builders" "follow-builders"
install_from_path "外部精选Skills/43-Agent-skills/media-transcriber" "media-transcriber"
install_from_path "外部精选Skills/43-Agent-skills/social-media-scout" "social-media-scout"
install_from_path "外部精选Skills/43-Agent-skills/video-creator" "video-creator"
install_from_path "外部精选Skills/43-Agent-skills/web-browser" "web-browser"
install_from_path "外部精选Skills/qiaomu-markdown-proxy" "qiaomu-markdown-proxy"
install_from_path "外部精选Skills/Skill-Vetter/skills/skill-vetter" "skill-vetter"
install_from_path "外部精选Skills/skill-creator" "skill-creator"
install_from_path "外部精选Skills/ian-xiaohei-illustrations" "ian-xiaohei-illustrations"
install_from_path "外部精选Skills/futurex-vc-skills/skills/pitch-deck-screening.md" "pitch-deck-screening"
install_from_path "外部精选Skills/futurex-vc-skills/skills/claims-verification.md" "claims-verification"
install_from_path "外部精选Skills/futurex-vc-skills/skills/risk-memo.md" "risk-memo"
install_from_path "外部精选Skills/futurex-vc-skills/skills/market-map.md" "market-map"
install_from_path "外部精选Skills/futurex-vc-skills/skills/startup-onepager.md" "startup-onepager"
install_from_path "外部精选Skills/futurex-vc-skills/skills/technical-dd.md" "technical-dd"
install_from_path "外部精选Skills/futurex-vc-skills/skills/memo-to-ic.md" "memo-to-ic"
install_from_path "外部精选Skills/futurex-vc-skills/skills/product-feedback-analysis.md" "product-feedback-analysis"
install_from_path "外部精选Skills/futurex-vc-skills/skills/paper-analysis.md" "paper-analysis"
install_from_path "外部精选Skills/futurex-vc-skills/skills/patent-analysis.md" "patent-analysis"
install_from_path "天际团队SKills库/TODO任务追踪" "TODO任务追踪"
install_from_path "天际团队SKills库/事项提醒" "事项提醒"
# CATALOG:END

if [ -z "$ONLY_SKILL" ] || [ "$ONLY_SKILL" = "fx-wechat-formatter" ]; then
    FX_FORMATTER_DIR="$AGENTS_DIR/fx-wechat-formatter"
    if [ -f "$FX_FORMATTER_DIR/SKILL.md" ]; then
        mkdir -p "$FX_FORMATTER_DIR/scripts"
        curl -fsSL "$RAW_BASE/天际团队SKills库/fx-wechat-formatter/scripts/build_docx.js" -o "$FX_FORMATTER_DIR/scripts/build_docx.js" || true
    fi
fi

echo "🎉 安装流程完成！"
