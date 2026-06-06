---
name: futurex-vc
description: Use for FutureX-style VC investment research workflows, including pitch deck screening, startup one-pagers, claim verification, market maps, risk memos, technical due diligence, product feedback analysis, paper analysis, patent analysis, and IC memo preparation. Use when the user asks to analyze startup materials, BP/decks, company claims, markets, competitors, technology evidence, due diligence findings, or prepare Chinese VC research outputs with evidence labels and confidentiality guardrails.
metadata:
  short-description: FutureX VC research workflows
---

# FutureX VC

This skill routes FutureX VC research requests to the right workflow while keeping sensitive deal materials local and evidence-labeled.

## Core Rules

1. Read `references/AGENTS.md` before doing substantive FutureX VC research.
2. Select only the workflow file needed for the task from `references/skills/`.
3. If the user explicitly names a workflow or file, read that file first.
4. Default to Chinese output unless the user asks otherwise.
5. Separate verified facts, company self-claims, third-party reporting, inference/judgment, and unverified items.
6. Do not invent revenue, customers, financing, valuation, market size, technical metrics, founder background, or legal conclusions.
7. Treat real BP/decks, financials, customer lists, contracts, interview notes, and internal memos as sensitive. Do not upload, publish, or commit them.

## Workflow Map

- Pitch deck or BP initial screening: `references/skills/pitch-deck-screening.md`
- Company one-pager: `references/skills/startup-onepager.md`
- Claims extraction and verification: `references/skills/claims-verification.md`
- Market map, value chain, and competitor landscape: `references/skills/market-map.md`
- Risk memo and mitigation plan: `references/skills/risk-memo.md`
- Technical due diligence: `references/skills/technical-dd.md`
- IC memo preparation: `references/skills/memo-to-ic.md`
- Product feedback and PMF signal analysis: `references/skills/product-feedback-analysis.md`
- Research paper investment analysis: `references/skills/paper-analysis.md`
- Patent moat and risk analysis: `references/skills/patent-analysis.md`

## Task Templates

If the user asks for a ready-to-run task prompt, adapt the corresponding file from `references/tasks/`. These templates are examples, not mandatory procedure.

## Output Handling

Save outputs where the user asks. If no destination is specified and a file deliverable is useful, use the current workspace `outputs/` folder. Before saving or sharing, check for unredacted sensitive company names, non-public deal data, personal information, or internal investment judgments.
