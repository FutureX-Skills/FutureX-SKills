---
name: linkedin-long-post
description: Convert raw notes or Chinese-language information into a polished English LinkedIn long-form essay. Trigger whenever the user pastes Chinese text, bullet points, or rough notes and asks to turn it into a post, or says things like "write a LinkedIn post", "help me post this", "convert this", "turn this into a post". Also trigger when user pastes any raw content (in any language) and seems to want a publishable write-up. Always output a full essay + hashtags ready to copy-paste onto LinkedIn.
---

# LinkedIn Long-Form Essay Skill

Take raw input — typically Chinese notes, bullet points, or rough ideas — and produce a polished, publish-ready English LinkedIn essay with hashtags. This is long-form thought leadership writing, not a short post. Think 400–800 words, with a real argument, structured sections, and a thesis that lands.

---

## Input Handling

- Input is often in Chinese, mixed Chinese/English, or rough bullet points
- Extract the core insight or argument from the raw material
- Do not translate literally — reframe into a compelling English narrative
- Find the angle that would resonate with a professional audience (founders, investors, operators)
- If the input is observational or data-rich, build an argument around it — don't just report it

---

## Essay Structure

**1. Opening reframe (1–2 short paragraphs)**
Start with a claim that inverts a common assumption or surfaces a hidden shift. No preamble, no "I've been thinking about..." — just the point. The first sentence has to earn the scroll.

LinkedIn cuts off after ~3 lines before "see more", so the very first line must be sharp enough to make someone click through.

**2. Body (4–8 short paragraphs with optional subheadings)**
- Use **declarative subheadings** when the essay has distinct sections — they orient the reader and make it scannable
- Each paragraph: 2–4 sentences max
- Short → short → medium rhythm throughout
- Tight logical progression — each paragraph earns the next
- Ground every abstract claim with a concrete example, number, or named system
- Name and correct the wrong version of your argument: "This is sometimes described as X. That framing misses the point."
- White space is your friend — line breaks make it readable on mobile

**3. Landing line**
The final line crystallizes the whole essay into one sentence. Make it quotable. This is what people screenshot and share.

---

## Voice & Tone

- **Practitioner voice** — written from inside the work, not above it
- **Confident, not arrogant.** State positions. Don't oversell.
- **No hedging.** "This market is moving." Not "it seems like this space might be evolving."
- **Active voice always.**
- **First-person is fine** — "I've seen this firsthand", "what struck me was" — but use sparingly to ground claims
- **Avoid:** "ecosystem", "paradigm", "unlock", "revolutionize", "game-changing", "excited to share", "thrilled to announce", excessive use of "AI" as a buzzword
- **Prefer:** Specific nouns, named companies, real numbers, named behaviors and tradeoffs

---

## Argumentation Style

1. **Open with the reframe** — invert a common assumption or surface a hidden shift
2. **Name and correct the wrong version** — "The obvious read is X. That misses the point."
3. **Examples as proof, not decoration** — every abstract claim needs a concrete anchor
4. **End with a compressed thesis** — one line that makes the whole thing land

---

## Formatting Rules

- No bullet-heavy sections — ideas live in sentences and paragraphs
- Tables are acceptable when showing a spectrum or taxonomy
- Subheadings are optional but useful for essays over 500 words
- The essay should read like something a thoughtful practitioner wrote, not a structured document or consulting deck

---

## Hashtags

After the essay, add a blank line and then 3–6 relevant hashtags.

Rules:
- Choose hashtags that are actually followed on LinkedIn (#venturecapital, #startups, #artificialintelligence, #founder, #investing, #deeptech, #fintech — pick what fits)
- Mix broad reach tags (#startups, #investing) with specific topic tags (#AIagents, #climatetech, etc.)
- No obscure or made-up hashtags
- Format: `#tag1 #tag2 #tag3`

---

## Output Format

```
[Sharp opening line / reframe]

[Opening paragraph(s)]

## [Optional subheading]

[Body paragraphs...]

[Landing line — one punchy sentence]

#hashtag1 #hashtag2 #hashtag3 #hashtag4
```

---

## Quick Checklist Before Outputting

- [ ] Does the very first line earn the "see more" click?
- [ ] Is there a real argument, not just observations?
- [ ] Are all paragraphs 4 sentences or fewer?
- [ ] Is every abstract point grounded by something concrete?
- [ ] Is the final line punchy and quotable?
- [ ] Have I removed all hedging, filler, and corporate speak?
- [ ] Are 3–6 relevant hashtags included at the end?
