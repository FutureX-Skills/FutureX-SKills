---
name: pib-search
description: PIB (Private Investment Banking) Search - Compile investment memos for private companies using search and web scraping. Generates concise VC-style reports focusing on recent developments (prioritizing <1 year old data), including investment highlights, operating/financial data, competitive landscape, and upside potential.
allowed-tools: web_search, kimi_search, web_fetch, kimi_fetch, exec
---

# PIB Search - Private Investment Banking Intelligence

Generate investment intelligence reports for private companies from a VC investor perspective.

## Capabilities

- **VC Investment Memo** — Structured investment analysis
- **Time-weighted research** — Prioritizes information <1 year old
- **Multi-source search** — English and Chinese sources
- **Latest news** — Last 7 days highlights

## Usage

```bash
# Generate VC investment memo
pib-search memo "Company Name"

# With focus on specific areas
pib-search memo "Company Name" --focus funding,competition

# Quick news only (last 7 days)
pib-search news "Company Name"
```

## Report Structure

### 1. Investment Highlights
- Funding history (last 12 months prioritized)
- Key investors and their stakes
- Valuation trajectory
- Use of funds / capital efficiency

### 2. Operating & Financial Data
- Revenue estimates (recent quarters)
- Growth metrics (YoY, QoQ)
- Unit economics (if available)
- Headcount / team growth
- Geographic expansion

### 3. Competitive Landscape
- Market positioning
- Key competitors
- Differentiation factors
- Market share estimates
- Moat analysis

### 4. Upside Potential
- Market size (TAM/SAM/SOM)
- Growth catalysts
- Expansion opportunities
- Exit potential (strategic buyers, IPO timeline)

### 5. Latest News (Last 7 Days)
- Funding announcements
- Product launches
- Partnerships
- Executive changes
- Market developments

## Data Sources

| Source | Language | Best For |
|--------|----------|----------|
| Crunchbase | EN | Funding, investors, valuations |
| TechCrunch | EN | Funding news, product launches |
| PitchBook | EN | Detailed financials, comps |
| LinkedIn | EN | Team growth, hiring |
| Tianyancha (天眼查) | ZH | Chinese company registry, ownership |
| 36kr | ZH | Chinese startup funding news |
| Sogou WeChat | ZH | Chinese market sentiment, announcements |

## Time Priority

| Data Age | Priority | Usage |
|----------|----------|-------|
| < 3 months | High | Core investment thesis |
| 3-12 months | Medium | Context and trends |
| > 12 months | Low | Background only |

## Notes

- Focuses on investable insights, not comprehensive data dumps
- Uses concise, investor-style language
- Flags data gaps and verification needs
- Prioritizes recent developments over historical data
