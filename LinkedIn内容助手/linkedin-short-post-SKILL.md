---
name: linkedin-short-post
description: Convert raw notes or Chinese-language information into a polished English LinkedIn short post with emoji section headers, numbered lists, and a closing question. Trigger whenever the user says "short post", "write a short LinkedIn post", "quick post", "shorter post", or pastes Chinese notes and wants something more structured and scannable (not an essay). Also trigger when the user wants a LinkedIn post that drives comments and engagement. Always output a full post + hashtags ready to copy-paste onto LinkedIn.
---

# LinkedIn Short Post Skill

Take raw input — typically Chinese notes, bullet points, or rough ideas — and produce a polished, publish-ready English LinkedIn short post. This is structured, scannable, engagement-optimized writing. Think 150–300 words max, emoji-anchored sections, and a closing question that drives comments. Keep it tight — if it's getting long, cut, don't pad.

---

## Input Handling

- Input is often in Chinese, mixed Chinese/English, or rough bullet points
- Extract the core thesis and 2–3 supporting points
- Do not translate literally — reframe into a punchy English narrative
- Find the provocative angle: the counterintuitive claim, the data point that surprises, the framing that reframes the debate

---

## Post Structure

**1. Hook line (1 sentence)**
The very first line is the headline. It should be a bold claim, a surprising stat, or a sharp reframe. No preamble. LinkedIn cuts off after ~3 lines — this line has to earn the "see more" click.

Example: *"The 'SaaSpocalypse' is a catchy headline, but the data suggests we aren't witnessing an ending. We're witnessing a massive structural repricing."*

**2. Setup (1–2 sentences)**
Briefly frame why this matters or what the tension is. Sets up the sections below.

**3. Emoji-anchored sections (2–4 sections)**
Each section follows this format:
```
[Emoji] [BOLD SECTION TITLE IN CAPS]
1–3 sentences of explanation or sub-points (can be numbered list)
```

Pick emojis that match the emotional tone of each section:
- 📉 for decline, data, drops
- 💸 for money, margins, economics
- 🏆 for winners, opportunity
- ⚠️ for risk, warning
- 🔄 for change, shift, transition
- 📊 for data, analysis
- 🚀 for growth, momentum
- 🤖 for AI, automation
- 💡 for insight, key takeaway
- 🧩 for complexity, nuance

Keep sections tight — 2–4 sentences or 2–3 numbered sub-points each. No bloat.

**4. Bottom Line block**
Close with a "The Bottom Line:" paragraph. 2–3 sentences max. Restate the thesis sharper. This is the takeaway someone would quote.

**5. Closing question**
End with one direct question to the reader. Make it specific enough to actually prompt a response — not "what do you think?" but something like "Are you seeing margin compression in your sector, or is the 'SaaSpocalypse' talk overblown?"

---

## Voice & Tone

- **Confident and direct.** Make claims. No hedging.
- **Data-grounded where possible.** Specific numbers beat vague assertions. "38% decline" beats "significant decline."
- **Active voice always.**
- **Avoid:** "excited to share", "thrilled to announce", "in today's rapidly evolving landscape", "it goes without saying"
- **Prefer:** Named trends, specific percentages, concrete company behaviors, vivid comparisons

---

## Formatting Rules

- Bold section titles under each emoji
- Numbered lists within sections when listing 2+ distinct sub-points
- Short paragraphs — 2–3 sentences max per block
- Lots of white space — one blank line between every section
- "The Bottom Line:" as a labeled closing block

---

## Hashtags

After the post, add a blank line and 4–6 relevant hashtags.

Rules:
- Mix broad reach (#AI, #SaaS, #VentureCapital) with specific topic tags (#CloudComputing, #TechTrends, #AIAgents)
- All lowercase or CamelCase — both are fine on LinkedIn
- No obscure or made-up hashtags
- Format: `#tag1 #tag2 #tag3 #tag4`

---

## Output Format

```
[Hook line — bold claim or surprising stat]

[1–2 sentence setup]

[Emoji] [BOLD TITLE]
[2–3 sentences or numbered sub-points]

[Emoji] [BOLD TITLE]
[2–3 sentences or numbered sub-points]

[Emoji] [BOLD TITLE]
[2–3 sentences or numbered sub-points]

The Bottom Line: [2–3 sentence sharp restatement of thesis]

[Closing question to drive comments]

#tag1 #tag2 #tag3 #tag4 #tag5
```

---

## Quick Checklist Before Outputting

- [ ] Does the first line earn the "see more" click?
- [ ] Are there 2–4 emoji-anchored sections?
- [ ] Is each section tight (2–4 sentences or numbered sub-points)?
- [ ] Is there a "The Bottom Line:" closing block?
- [ ] Does the post end with a specific, engaging question?
- [ ] Are 4–6 relevant hashtags included?
- [ ] Have I removed all hedging, filler, and corporate speak?
