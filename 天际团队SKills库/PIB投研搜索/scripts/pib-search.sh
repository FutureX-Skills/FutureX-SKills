#!/bin/bash
# PIB Search - Private Investment Banking Intelligence Tool
# Gathers public information about private companies for investment analysis

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
COMPANY=""
MODE="search"
SOURCES=""
DAYS=30
VERBOSE=false

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

usage() {
    echo "PIB Search - Private Investment Banking Intelligence"
    echo ""
    echo "Usage:"
    echo "  pib-search search \"Company Name\"     Quick search (EN + ZH sources)"
    echo "  pib-search deep \"Company Name\"       Deep dive with scraping"
    echo "  pib-search news \"Company Name\"       Recent news only"
    echo "  pib-search people \"Company Name\"     Find key personnel"
    echo "  pib-search memo \"Company Name\"       Generate VC investment memo"
    echo ""
    echo "Options:"
    echo "  --sources list    Comma-separated sources (crunchbase,tianyancha,...)"
    echo "  --days N          News lookback period (default: 30)"
    echo "  --verbose         Detailed output"
    echo ""
    echo "Examples:"
    echo "  pib-search search \"ByteDance\""
    echo "  pib-search deep \"OpenAI\" --sources crunchbase"
    echo "  pib-search news \"Stripe\" --days 7"
    echo "  pib-search memo \"Shein\"              # VC investment memo"
}

log() {
    if [ "$VERBOSE" = true ]; then
        echo -e "${BLUE}[INFO]${NC} $1"
    fi
}

warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Parse arguments
parse_args() {
    MODE="$1"
    shift
    
    # Find company name (first non-flag argument)
    while [[ $# -gt 0 ]]; do
        case "$1" in
            --sources)
                SOURCES="$2"
                shift 2
                ;;
            --days)
                DAYS="$2"
                shift 2
                ;;
            --verbose)
                VERBOSE=true
                shift
                ;;
            --help|-h)
                usage
                exit 0
                ;;
            -*)
                error "Unknown option: $1"
                usage
                exit 1
                ;;
            *)
                if [ -z "$COMPANY" ]; then
                    COMPANY="$1"
                fi
                shift
                ;;
        esac
    done
    
    if [ -z "$COMPANY" ]; then
        error "Company name required"
        usage
        exit 1
    fi
}

# Quick search across sources
quick_search() {
    local company="$1"
    echo "🔍 Searching for: $company"
    echo ""
    
    # English sources
    echo -e "${GREEN}=== English Sources ===${NC}"
    echo ""
    
    echo "📰 General Search:"
    echo "  Google: https://www.google.com/search?q=$(echo "$company" | sed 's/ /+/g')+company"
    echo "  Bing: https://www.bing.com/search?q=$(echo "$company" | sed 's/ /+/g')+company"
    echo ""
    
    echo "💰 Funding/Startup Data:"
    echo "  Crunchbase: https://www.crunchbase.com/organization/$(echo "$company" | tr '[:upper:]' '[:lower:]' | sed 's/ /-/g')"
    echo "  PitchBook: https://pitchbook.com/profiles/search?q=$(echo "$company" | sed 's/ /%20/g')"
    echo ""
    
    echo "📰 Tech News:"
    echo "  TechCrunch: https://techcrunch.com/?s=$(echo "$company" | sed 's/ /+/g')"
    echo ""
    
    echo "💼 Professional:"
    echo "  LinkedIn: https://www.linkedin.com/company/$(echo "$company" | tr '[:upper:]' '[:lower:]' | sed 's/ //g')"
    echo ""
    
    # Chinese sources
    echo -e "${GREEN}=== Chinese Sources ===${NC}"
    echo ""
    
    echo "🔍 搜索 (Search):"
    echo "  Baidu: https://www.baidu.com/s?wd=$(echo "$company" | sed 's/ /+/g')"
    echo ""
    
    echo "🏢 企业信息 (Company Registry):"
    echo "  天眼查: https://www.tianyancha.com/search?key=$(echo "$company" | sed 's/ /%20/g')"
    echo "  企查查: https://www.qcc.com/search?key=$(echo "$company" | sed 's/ /%20/g')"
    echo ""
    
    echo "📰 科技新闻 (Tech News):"
    echo "  36氪: https://36kr.com/search/articles/$(echo "$company" | sed 's/ /%20/g')"
    echo "  虎嗅: https://www.huxiu.com/search?key=$(echo "$company" | sed 's/ /%20/g')"
    echo ""
    
    echo "💬 社交媒体 (Social Media):"
    echo "  搜狗微信 (WeChat Articles): https://weixin.sogou.com/weixin?type=2&query=$(echo "$company" | sed 's/ /+/g')"
    echo "     → Best for finding WeChat public account articles"
    echo ""
    
    echo -e "${YELLOW}Tip:${NC} Use 'pib-search deep \"$company\"' to scrape these sources"
    echo -e "${YELLOW}Tip:${NC} Use 'pib-search memo \"$company\"' for VC investment memo"
}

# Deep dive with scraping
deep_dive() {
    local company="$1"
    echo "🔎 Deep Dive: $company"
    echo ""
    
    # Check if scrapling is available
    SCRAPLING_TOOL="/root/.openclaw/skills/scrapling/scrapling-tool.py"
    if [ ! -f "$SCRAPLING_TOOL" ]; then
        warn "Scrapling not found at $SCRAPLING_TOOL"
        warn "Install scrapling skill for full functionality"
        echo ""
    fi
    
    # Determine sources
    if [ -z "$SOURCES" ]; then
        SOURCES="crunchbase,tianyancha"
    fi
    
    IFS=',' read -ra SOURCE_LIST <<< "$SOURCES"
    
    for source in "${SOURCE_LIST[@]}"; do
        case "$source" in
            crunchbase)
                scrape_crunchbase "$company"
                ;;
            tianyancha)
                scrape_tianyancha "$company"
                ;;
            *)
                warn "Unknown source: $source"
                ;;
        esac
    done
}

# Scrape Crunchbase
scrape_crunchbase() {
    local company="$1"
    local slug=$(echo "$company" | tr '[:upper:]' '[:lower:]' | sed 's/ /-/g' | sed 's/[^a-z0-9-]//g')
    local url="https://www.crunchbase.com/organization/$slug"
    
    echo -e "${GREEN}=== Crunchbase: $company ===${NC}"
    echo "URL: $url"
    echo ""
    
    # Note: Crunchbase has strong anti-bot, recommend manual visit
    echo -e "${YELLOW}Note:${NC} Crunchbase has anti-bot protection."
    echo "Recommended: Visit manually or use their API"
    echo ""
}

# Scrape Tianyancha
scrape_tianyancha() {
    local company="$1"
    local encoded=$(echo "$company" | sed 's/ /%20/g')
    local url="https://www.tianyancha.com/search?key=$encoded"
    
    echo -e "${GREEN}=== 天眼查 (Tianyancha): $company ===${NC}"
    echo "URL: $url"
    echo ""
    
    # Note: Tianyancha requires login for details
    echo -e "${YELLOW}Note:${NC} Tianyancha requires login for detailed data."
    echo "Search URL provided above for manual verification."
    echo ""
}

# Find news
find_news() {
    local company="$1"
    echo "📰 Recent News: $company (last $DAYS days)"
    echo ""
    
    # English news
    echo -e "${GREEN}=== English News ===${NC}"
    echo "Google News: https://news.google.com/search?q=$(echo "$company" | sed 's/ /+/g')+when%3A${DAYS}d"
    echo "TechCrunch: https://techcrunch.com/?s=$(echo "$company" | sed 's/ /+/g')"
    echo ""
    
    # Chinese news
    echo -e "${GREEN}=== 中文新闻 ===${NC}"
    echo "百度新闻: https://news.baidu.com/ns?word=$(echo "$company" | sed 's/ /+/g')&bt=$DAYS"
    echo "搜狗微信 (WeChat): https://weixin.sogou.com/weixin?type=2&query=$(echo "$company" | sed 's/ /+/g')"
    echo ""
}

# Find people
find_people() {
    local company="$1"
    echo "👥 Key People: $company"
    echo ""
    
    echo -e "${GREEN}=== Sources ===${NC}"
    echo "LinkedIn: https://www.linkedin.com/company/$(echo "$company" | tr '[:upper:]' '[:lower:]' | sed 's/ //g')/people/"
    echo "Crunchbase (founders): https://www.crunchbase.com/organization/$(echo "$company" | tr '[:upper:]' '[:lower:]' | sed 's/ /-/g')"
    echo ""
}

# Generate VC investment memo
generate_memo() {
    local company="$1"
    local script_dir="$(dirname "$0")"
    
    echo "📊 Generating VC Investment Memo: $company"
    echo ""
    
    if [ -f "$script_dir/vc-memo.py" ]; then
        python3 "$script_dir/vc-memo.py" "$company"
    else
        error "VC memo generator not found at $script_dir/vc-memo.py"
        exit 1
    fi
}

# Main
# If first argument is a mode, use it; otherwise default to search
if [ $# -gt 0 ] && [[ "$1" =~ ^(search|deep|news|people|memo|help|-h|--help)$ ]]; then
    MODE="$1"
fi

case "$MODE" in
    search)
        parse_args "$@"
        quick_search "$COMPANY"
        ;;
    deep)
        parse_args "$@"
        deep_dive "$COMPANY"
        ;;
    news)
        parse_args "$@"
        find_news "$COMPANY"
        ;;
    people)
        parse_args "$@"
        find_people "$COMPANY"
        ;;
    memo)
        parse_args "$@"
        generate_memo "$COMPANY"
        ;;
    help|--help|-h)
        usage
        ;;
    *)
        error "Unknown mode: $MODE"
        usage
        exit 1
        ;;
esac
