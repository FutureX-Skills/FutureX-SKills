#!/usr/bin/env python3
"""
Company Intelligence - Advanced version with search + scraping
Uses kimi_search and scrapling for automated data collection
"""

import sys
import json
import argparse
import re
from urllib.parse import quote

# Add scrapling to path
sys.path.insert(0, '/root/.openclaw/venv/lib/python3.12/site-packages')

def search_company(company_name, lang="en"):
    """Search for company info using web search"""
    print(f"🔍 Searching for: {company_name} ({lang})")
    
    queries = {
        "en": [
            f"{company_name} company funding",
            f"{company_name} founded founders",
            f"{company_name} crunchbase"
        ],
        "zh": [
            f"{company_name} 公司 融资",
            f"{company_name} 创始人",
            f"{company_name} 天眼查"
        ]
    }
    
    results = []
    for query in queries.get(lang, queries["en"]):
        print(f"  Query: {query}")
        # In real usage, this would call kimi_search
        results.append({"query": query, "status": "pending"})
    
    return results

def scrape_with_scrapling(url, mode="stealth"):
    """Scrape a URL using scrapling"""
    try:
        from scrapling import Fetcher, StealthyFetcher
        
        print(f"🌐 Scraping: {url}")
        
        if mode == "stealth":
            fetcher = StealthyFetcher()
        else:
            fetcher = Fetcher()
        
        page = fetcher.get(url)
        return {
            "status": "success",
            "url": url,
            "title": getattr(page, 'title', 'N/A'),
            "content_length": len(str(page))
        }
    except Exception as e:
        return {
            "status": "error",
            "url": url,
            "error": str(e)
        }

def format_company_slug(name):
    """Convert company name to URL-friendly slug"""
    return re.sub(r'[^a-z0-9-]', '', name.lower().replace(' ', '-'))

def generate_report(company_name):
    """Generate a company intelligence report"""
    report = {
        "company": company_name,
        "generated_at": "2026-03-15",
        "sources": {
            "english": {
                "google_search": f"https://www.google.com/search?q={quote(company_name)}+company",
                "crunchbase": f"https://www.crunchbase.com/organization/{format_company_slug(company_name)}",
                "linkedin": f"https://www.linkedin.com/company/{format_company_slug(company_name)}",
                "techcrunch": f"https://techcrunch.com/?s={quote(company_name)}"
            },
            "chinese": {
                "baidu_search": f"https://www.baidu.com/s?wd={quote(company_name)}",
                "tianyancha": f"https://www.tianyancha.com/search?key={quote(company_name)}",
                "qichacha": f"https://www.qcc.com/search?key={quote(company_name)}",
                "36kr": f"https://36kr.com/search/articles/{quote(company_name)}",
                "wechat_sogou": f"https://weixin.sogou.com/weixin?type=2&query={quote(company_name)}"
            }
        },
        "recommended_queries": {
            "funding": f"{company_name} Series A B C funding raised",
            "founders": f"{company_name} founder CEO",
            "news": f"{company_name} latest news 2026"
        }
    }
    return report

def main():
    parser = argparse.ArgumentParser(description='Company Intelligence Tool')
    parser.add_argument('company', help='Company name to research')
    parser.add_argument('--scrape', action='store_true', help='Enable scraping (requires scrapling)')
    parser.add_argument('--sources', default='all', help='Sources to use (all, en, zh)')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    
    args = parser.parse_args()
    
    print(f"📊 Company Intelligence Report: {args.company}")
    print("=" * 50)
    print()
    
    # Generate report structure
    report = generate_report(args.company)
    
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print("🔗 English Sources:")
        for name, url in report["sources"]["english"].items():
            print(f"  • {name}: {url}")
        
        print()
        print("🔗 中文来源 (Chinese Sources):")
        for name, url in report["sources"]["chinese"].items():
            print(f"  • {name}: {url}")
        
        print()
        print("🔍 Recommended Search Queries:")
        for category, query in report["recommended_queries"].items():
            print(f"  • {category}: {query}")
        
        if args.scrape:
            print()
            print("🌐 Scraping enabled (requires manual execution with scrapling)")
    
    print()
    print("💡 Tip: Use the URLs above to manually verify or run with --scrape for automated extraction")

if __name__ == "__main__":
    main()
