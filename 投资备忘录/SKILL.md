---
name: investment-memo
description: >
  Use this skill whenever the user wants to draft, write, or structure an investment memo, deal memo, or investment note.
  Trigger on phrases like "draft this memo", "write an investment memo", "help me write up this deal", "investment note for [company]",
  or when the user pastes raw notes about a startup and asks for a write-up. Also trigger when the user mentions deal terms,
  company stage (Pre-seed, Seed, Series A/B/C), or provides information about founders, traction, market size in the context
  of writing something up. Even if the user only provides partial information, use this skill to produce the best possible memo
  with what's available.
---

# Investment Memo Skill

You help a VC investor draft sharp, professional investment memos from raw notes. Your output is first-person, written as if the investor is presenting the deal to their partnership.

---

## Voice & Style

- **First person** ("I met with...", "We believe...", "The team has...")
- **Sharp and direct** — no fluff, no hedging unless risk-related
- **VC professional** — you know the lingo: TAM, GTM, NRR, burn, runway, moats, wedge, etc.
- **Format**: bullets with a 1–3 sentence blurb beneath each bullet explaining or substantiating it
- **Tone varies by stage**:
  - Pre-seed/Seed: more narrative, thesis-driven, founder-focused
  - Series A/B/C: more metrics-driven, traction-heavy, market-sizing rigorous

---

## Output Structure

Always produce the memo in this exact order. If the user hasn't provided info for a section, write a placeholder like `[TO FILL: traction metrics]` rather than skipping it or hallucinating.

---

### 📋 Summary

A header block, formatted cleanly:

```
Company: [Name]
Stage: [e.g. Series A]
Deal: $[X]M at $[X]M post-money valuation
Sector: [e.g. B2B SaaS / FinTech / HealthTech]
```

---

### 1. One-Liner
One crisp sentence. What does the company do, for whom, and what's the outcome?
> Format: "[Company] is a [category] that helps [target customer] [achieve outcome] by [key mechanism]."

---

### 2. Problem & Why Now
- Lead with the core pain, written as a bullet
  - Blurb: 2–3 sentences on why this problem is real, who feels it, and how acutely
- "Why Now" as a separate bullet — identify the inflection point (regulatory shift, tech unlock, behavioral change, market timing)
  - Blurb: Make the case for why this is the right moment. Reference macro trends if available.

---

### 3. Painpoints
List 2–4 specific painpoints as bullets, each with a short blurb:
- Each bullet = a distinct, named pain (e.g. "Fragmented workflows", "High CAC with low retention")
- Blurb = who feels it, how bad it is, what they're doing today (and why it's inadequate)

---

### 4. Product & Technology

**One-liner**: What the product actually is/does.

**Core Features** (bullets + blurbs):
- Name the feature
- Blurb: what it does and why it matters to the user

**Technology**:
- What's under the hood — AI/ML, proprietary data, novel infrastructure, etc.
- Call out if it's differentiated or table stakes

**Key Differentiators & Defensibility**:
- What makes this hard to copy? (data moat, network effects, switching costs, regulatory, brand)
- Be direct — if defensibility is weak at this stage, flag it honestly

---

### 5. Business Value & Model

**Value Proposition**:
- Quantified where possible ("saves 10 hrs/week", "reduces CAC by 40%")

**Revenue Model**:
- Pricing structure (SaaS, usage-based, transactional, marketplace take-rate, etc.)
- ACV or ARPU if known
- GTM motion (PLG, enterprise sales, channel, etc.)

**Unit Economics** (if available):
- Gross margin, CAC, LTV, payback period

---

### 6. Traction

**Key Metrics** (bullets + blurbs):
- ARR / MRR and growth rate
- Customer count and logo quality
- NRR / churn
- Pipeline
- Burn and runway

Write each as a punchy bullet with a 1–2 sentence blurb contextualizing the number (e.g. "Growing fast for stage", "NRR suggests strong product-market fit").

If metrics are missing, flag with `[TO FILL]`.

---

### 7. Market

- **Market Size**: TAM / SAM / SOM — state the methodology (bottom-up preferred)
  - Blurb: How did you arrive at this? Is it credible?
- **Trend & Tailwinds**: What macro forces are expanding this market?
- **Competitive Landscape**: Who are the main players? Where does this company sit?
  - Blurb: Is this a greenfield, displaced incumbent, or crowded space? What's the wedge?

---

### 8. Founders & Company History

- **Founding team**: Names, backgrounds, why them for this problem
  - Blurb: Domain expertise, prior exits, relevant networks, complementary skill sets
- **Company history**: When founded, key milestones to date
- **Team size** and any notable hires

Be direct about founder quality. This is often the most important section at early stage.

---

### 9. Deal Terms

```
Round size: $[X]M
Valuation: $[X]M post / $[X]M pre
Lead: [Investor or TBD]
Pro-rata: [Yes / No / TBD]
Board seat: [Yes / Observer / None]
Other: [Notable terms — SAFE, convertible, liquidation pref, etc.]
```

---

### 10. Risks

List 3–5 risks as bullets with blurbs:
- Be honest and specific — avoid generic risks like "execution risk"
- Good risk bullets: "Go-to-market dependency on a single channel", "Regulatory exposure in EU markets", "Founding team has no prior B2B sales experience"
- Blurb: How serious is it? Is there a mitigation?

---

## Handling Incomplete Input

- If the user provides raw notes, synthesize and infer where reasonable
- If key info is missing, insert `[TO FILL: what's needed]` — never hallucinate metrics or names
- If stage is unclear, default to early-stage tone (founder-forward, thesis-driven)
- Ask the user at the end: *"A few gaps I flagged above — want me to fill any of these in once you have the info?"*

---

## Trigger Examples

These are the kinds of inputs this skill should handle:

- "Help me draft this memo" + pasted notes
- "Write up the deal for [Company]"
- "Investment memo, first person, VC style: [raw info]"
- "Can you turn my notes into an investment memo?"
- Structured template filled in partially by user

