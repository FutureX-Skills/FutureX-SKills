#!/usr/bin/env python3
"""
Company Intelligence - VC Investment Memo Generator
Generates investment-focused reports for private companies
"""

import sys
import json
import argparse
import re
from urllib.parse import quote
from datetime import datetime, timedelta

# Add scrapling to path
sys.path.insert(0, '/root/.openclaw/venv/lib/python3.12/site-packages')

def format_company_slug(name):
    """Convert company name to URL-friendly slug"""
    return re.sub(r'[^a-z0-9-]', '', name.lower().replace(' ', '-'))

def generate_vc_memo(company_name):
    """Generate VC investment memo structure"""
    
    memo = {
        "report_type": "VC Investment Memo",
        "company": company_name,
        "generated_at": datetime.now().strftime("%Y-%m-%d"),
        "data_freshness_priority": "< 12 months (prioritized), > 12 months (background)",
        
        "executive_summary": {
            "investment_thesis": "[To be filled with research]",
            "key_metrics": "[Revenue, growth, valuation]",
            "recommendation": "[Pass/Watch/Invest]"
        },
        
        "investment_highlights": {
            "funding_history": {
                "latest_round": "[Most recent funding round]",
                "valuation": "[Current/post-money valuation]",
                "key_investors": ["[Lead investor]", "[Follow-on investors]"],
                "total_raised": "[Lifetime funding]",
                "sources": [
                    f"https://www.crunchbase.com/organization/{format_company_slug(company_name)}",
                    f"https://techcrunch.com/?s={quote(company_name)}+funding"
                ]
            },
            "capital_efficiency": "[Burn rate, runway, unit economics]",
            "use_of_funds": "[How recent capital is being deployed]"
        },
        
        "operating_financial_data": {
            "revenue": {
                "latest_estimate": "[Annual/ARR estimate]",
                "growth_rate": "[YoY growth %]",
                "confidence": "[High/Medium/Low based on source quality]"
            },
            "key_metrics": {
                "customers": "[Customer count / logo]",
                "acv": "[Average contract value]",
                "retention": "[Net/Gross retention if available]"
            },
            "team": {
                "headcount": "[Current team size]",
                "growth": "[Hiring velocity from LinkedIn]",
                "key_hires": "[Recent executive additions]"
            },
            "geographic_presence": "[Markets of operation]",
            "sources": [
                f"https://www.linkedin.com/company/{format_company_slug(company_name)}",
                f"https://www.pitchbook.com/profiles/search?q={quote(company_name)}"
            ]
        },
        
        "competitive_landscape": {
            "market_position": "[Leader/Challenger/Niche]",
            "key_competitors": [
                {"name": "[Competitor 1]", "differentiation": "[Key difference]"},
                {"name": "[Competitor 2]", "differentiation": "[Key difference]"}
            ],
            "moat_analysis": "[Defensibility: tech, network effects, brand, switching costs]",
            "market_share": "[Estimated share if available]",
            "competitive_threats": "[Risks from incumbents/new entrants]"
        },
        
        "upside_potential": {
            "market_size": {
                "tam": "[Total Addressable Market]",
                "sam": "[Serviceable Available Market]", 
                "som": "[Serviceable Obtainable Market]"
            },
            "growth_catalysts": [
                "[Catalyst 1: New products, markets, partnerships]",
                "[Catalyst 2: Regulatory tailwinds, market shifts]"
            ],
            "expansion_opportunities": "[Geographic, vertical, product expansion]",
            "exit_potential": {
                "strategic_buyers": ["[Likely acquirers]"],
                "ipo_timeline": "[Estimated IPO readiness]",
                "comparable_exits": ["[Recent M&A/IPO comps]"]
            }
        },
        
        "latest_news_7d": {
            "period": "Last 7 days",
            "sources": [
                f"https://news.google.com/search?q={quote(company_name)}+when%3A7d",
                f"https://techcrunch.com/?s={quote(company_name)}",
                f"https://weixin.sogou.com/weixin?type=2&query={quote(company_name)}"
            ],
            "highlights": [
                "[Check sources above for: funding, product launches, partnerships, executive changes]"
            ]
        },
        
        "risk_factors": {
            "execution_risk": "[Team/operational risks]",
            "market_risk": "[Competition, market timing]",
            "financial_risk": "[Burn rate, path to profitability]",
            "regulatory_risk": "[Compliance, policy changes]"
        },
        
        "research_checklist": {
            "priority_sources": [
                f"☐ Crunchbase: https://www.crunchbase.com/organization/{format_company_slug(company_name)}",
                f"☐ TechCrunch: https://techcrunch.com/?s={quote(company_name)}",
                f"☐ LinkedIn: https://www.linkedin.com/company/{format_company_slug(company_name)}",
                f"☐ PitchBook: https://www.pitchbook.com/profiles/search?q={quote(company_name)}",
                f"☐ 天眼查: https://www.tianyancha.com/search?key={quote(company_name)}",
                f"☐ 36氪: https://36kr.com/search/articles/{quote(company_name)}",
                f"☐ 搜狗微信: https://weixin.sogou.com/weixin?type=2&query={quote(company_name)}"
            ],
            "key_questions": [
                "☐ What was the most recent funding round and valuation?",
                "☐ What is the current revenue run-rate and growth?",
                "☐ Who are the top 3 competitors and how do they compare?",
                "☐ What is the core moat/defensibility?",
                "☐ What are the biggest risks to the investment thesis?",
                "☐ Any recent news (last 7 days) that changes the picture?"
            ]
        }
    }
    
    return memo

def format_vc_memo_text(memo):
    """Format memo as readable text"""
    
    lines = []
    lines.append("=" * 70)
    lines.append(f"VC INVESTMENT MEMO: {memo['company']}")
    lines.append(f"Generated: {memo['generated_at']} | Data Priority: <12 months")
    lines.append("=" * 70)
    lines.append("")
    
    # Executive Summary
    lines.append("## EXECUTIVE SUMMARY")
    lines.append("-" * 40)
    lines.append(f"Investment Thesis: {memo['executive_summary']['investment_thesis']}")
    lines.append(f"Key Metrics: {memo['executive_summary']['key_metrics']}")
    lines.append(f"Recommendation: {memo['executive_summary']['recommendation']}")
    lines.append("")
    
    # Investment Highlights
    lines.append("## 1. INVESTMENT HIGHLIGHTS")
    lines.append("-" * 40)
    fh = memo['investment_highlights']['funding_history']
    lines.append(f"Latest Round: {fh['latest_round']}")
    lines.append(f"Valuation: {fh['valuation']}")
    lines.append(f"Key Investors: {', '.join(fh['key_investors'])}")
    lines.append(f"Total Raised: {fh['total_raised']}")
    lines.append(f"Capital Efficiency: {memo['investment_highlights']['capital_efficiency']}")
    lines.append(f"Sources: {', '.join(fh['sources'])}")
    lines.append("")
    
    # Operating & Financial
    lines.append("## 2. OPERATING & FINANCIAL DATA")
    lines.append("-" * 40)
    rev = memo['operating_financial_data']['revenue']
    lines.append(f"Revenue: {rev['latest_estimate']} (Growth: {rev['growth_rate']}, Confidence: {rev['confidence']})")
    
    km = memo['operating_financial_data']['key_metrics']
    lines.append(f"Customers: {km['customers']} | ACV: {km['acv']} | Retention: {km['retention']}")
    
    team = memo['operating_financial_data']['team']
    lines.append(f"Team: {team['headcount']} headcount | Growth: {team['growth']}")
    lines.append(f"Key Hires: {team['key_hires']}")
    lines.append(f"Geographic: {memo['operating_financial_data']['geographic_presence']}")
    lines.append("")
    
    # Competitive Landscape
    lines.append("## 3. COMPETITIVE LANDSCAPE")
    lines.append("-" * 40)
    cl = memo['competitive_landscape']
    lines.append(f"Market Position: {cl['market_position']}")
    lines.append("Key Competitors:")
    for comp in cl['key_competitors']:
        lines.append(f"  • {comp['name']}: {comp['differentiation']}")
    lines.append(f"Moat: {cl['moat_analysis']}")
    lines.append(f"Market Share: {cl['market_share']}")
    lines.append(f"Threats: {cl['competitive_threats']}")
    lines.append("")
    
    # Upside Potential
    lines.append("## 4. UPSIDE POTENTIAL")
    lines.append("-" * 40)
    ms = memo['upside_potential']['market_size']
    lines.append(f"Market Size: TAM {ms['tam']} | SAM {ms['sam']} | SOM {ms['som']}")
    lines.append("Growth Catalysts:")
    for cat in memo['upside_potential']['growth_catalysts']:
        lines.append(f"  • {cat}")
    lines.append(f"Expansion: {memo['upside_potential']['expansion_opportunities']}")
    
    ep = memo['upside_potential']['exit_potential']
    lines.append(f"Strategic Buyers: {', '.join(ep['strategic_buyers'])}")
    lines.append(f"IPO Timeline: {ep['ipo_timeline']}")
    lines.append("")
    
    # Latest News
    lines.append("## 5. LATEST NEWS (Last 7 Days)")
    lines.append("-" * 40)
    lines.append("Priority Sources:")
    for src in memo['latest_news_7d']['sources']:
        lines.append(f"  • {src}")
    lines.append("Check for: funding, product launches, partnerships, executive changes")
    lines.append("")
    
    # Risk Factors
    lines.append("## 6. RISK FACTORS")
    lines.append("-" * 40)
    rf = memo['risk_factors']
    lines.append(f"Execution: {rf['execution_risk']}")
    lines.append(f"Market: {rf['market_risk']}")
    lines.append(f"Financial: {rf['financial_risk']}")
    lines.append(f"Regulatory: {rf['regulatory_risk']}")
    lines.append("")
    
    # Research Checklist
    lines.append("## RESEARCH CHECKLIST")
    lines.append("-" * 40)
    lines.append("Priority Sources:")
    for src in memo['research_checklist']['priority_sources']:
        lines.append(f"  {src}")
    lines.append("")
    lines.append("Key Questions:")
    for q in memo['research_checklist']['key_questions']:
        lines.append(f"  {q}")
    
    lines.append("")
    lines.append("=" * 70)
    lines.append("FILL IN THE TEMPLATES ABOVE WITH DATA FROM SOURCES")
    lines.append("Prioritize information from the last 12 months")
    lines.append("=" * 70)
    
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description='VC Investment Memo Generator')
    parser.add_argument('company', help='Company name to research')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    parser.add_argument('--focus', default='all', help='Focus areas: funding,ops,competition,upside,news')
    
    args = parser.parse_args()
    
    memo = generate_vc_memo(args.company)
    
    if args.json:
        print(json.dumps(memo, indent=2, ensure_ascii=False))
    else:
        print(format_vc_memo_text(memo))

if __name__ == "__main__":
    main()
