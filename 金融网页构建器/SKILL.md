---
name: web-artifacts-builder
description: Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts requiring state management, routing, or shadcn/ui components - not for simple single-file HTML/JSX artifacts.
license: Complete terms in LICENSE.txt
---

# Web Artifacts Builder

To build powerful frontend claude.ai artifacts, follow these steps:
1. Initialize the frontend repo using `scripts/init-artifact.sh`
2. Develop your artifact by editing the generated code
3. Bundle all code into a single HTML file using `scripts/bundle-artifact.sh`
4. Display artifact to user
5. (Optional) Test the artifact

**Stack**: React 18 + TypeScript + Vite + Parcel (bundling) + Tailwind CSS + shadcn/ui

## Design & Style Guidelines

VERY IMPORTANT: All artifacts must adhere to a **Goldman Sachs institutional design system** — analytical, data-dense, and authoritative. This is the firm's visual identity: precision over decoration, hierarchy over ornamentation, signal over noise.

### Design Philosophy: Goldman Sachs Institutional Standard

Think: Prime brokerage terminal. Research portal. Executive dashboard. Every pixel earns its place.

#### Color Palette
```
--gs-navy:        #041C2C   /* Primary background — deep midnight navy */
--gs-navy-mid:    #0A2D45   /* Card/panel backgrounds */
--gs-navy-light:  #0D3559   /* Hover states, secondary panels */
--gs-slate:       #1A4A6E   /* Borders, dividers, subtle separators */
--gs-blue-accent: #0066CC   /* Primary action, links, highlights */
--gs-gold:        #B8960C   /* Premium accent — use sparingly */
--gs-white:       #F5F7FA   /* Primary text on dark */
--gs-muted:       #8FA8BE   /* Secondary text, labels, metadata */
--gs-dim:         #5C7A94   /* Tertiary / disabled */
--gs-green:       #00A878   /* Positive delta, gain */
--gs-red:         #D94F4F   /* Negative delta, loss, alert */
--gs-border:      rgba(255,255,255,0.08)  /* Subtle panel borders */
```

Default to **dark theme** (navy backgrounds). Light surfaces are used only for data-entry forms or specific modal contexts.

#### Typography
```
Display / Headline:  'Goldman Sans', 'Neue Haas Grotesk', 'Helvetica Neue', sans-serif
                     — weight 300 or 400, tracking: -0.02em
Data / Tabular:      'IBM Plex Mono', 'Courier New', monospace
                     — for all numbers, tickers, metrics, percentages
Body / Labels:       'Helvetica Neue', 'Arial', sans-serif — weight 400
```

Import from Google Fonts: `IBM Plex Mono` for all numeric/data values. Pair with `Helvetica Neue` or `Arial` for body. **Never use Inter, Roboto, or rounded display fonts.**

#### Layout Rules
- **Sharp corners only** — `border-radius: 0` everywhere except small pill badges (`border-radius: 2px` max)
- **Grid-based, left-aligned** — no centered hero layouts; data anchors left
- **Dense information display** — minimal padding (8px/12px), tight line-heights (1.3–1.4)
- **Thin dividers** — `1px solid var(--gs-border)` between sections, no thick separators
- **No decorative elements** — no gradients, no shadows beyond `0 1px 3px rgba(0,0,0,0.4)`, no illustrations
- **Micro-typography precision** — all numbers right-aligned in tables, monospace font, consistent decimal places

#### Component Patterns
```
Tables:        Alternating row shading (#041C2C / #0A2D45), sticky headers, sortable columns
               Right-align all numeric columns, monospace font
Metrics cards: Top-aligned label (11px, uppercase, letter-spacing: 0.08em, --gs-muted)
               Large value (24–32px, --gs-white, IBM Plex Mono)
               Delta below (12px, green/red with ▲▼ arrows)
Charts:        Navy background, thin axis lines (--gs-slate), no grid fill
               Line charts preferred; area fills use 10% opacity
Badges/Tags:   `border: 1px solid`, no fill, 2px radius, uppercase 10px text
Navigation:    Left sidebar or top bar — dark navy, thin bottom border
Buttons:       Outlined preferred (`border: 1px solid --gs-blue-accent`) or flat text links
               Filled buttons only for primary CTA, use --gs-blue-accent fill
```

#### Motion & Interaction
- Transitions: `150ms ease` — fast, crisp, professional
- No bouncy/elastic animations
- Hover states: subtle background shift (`--gs-navy-light`), no scale transforms
- Data loading: skeleton shimmer in `--gs-slate` tone only

#### What to NEVER do
- ❌ Purple, pink, teal, or rainbow gradients  
- ❌ Rounded cards (`border-radius > 4px`)  
- ❌ Drop shadows heavier than `0 2px 8px rgba(0,0,0,0.3)`  
- ❌ Centered hero sections or large decorative imagery  
- ❌ Sans-serif fonts for numeric data (always use monospace)  
- ❌ Bright saturated colors as backgrounds  
- ❌ Playful micro-interactions or bouncy animations  
- ❌ Emojis, icons as primary content (use sparingly — Lucide icons at 16px max)

#### The Standard to Hit
Every artifact should look like it could run on a Bloomberg terminal or inside GS Marquee — institutional, trustworthy, precision-engineered. If it could belong in a consumer app, redesign it.

## Quick Start

### Step 1: Initialize Project

Run the initialization script to create a new React project:
```bash
bash scripts/init-artifact.sh <project-name>
cd <project-name>
```

This creates a fully configured project with:
- ✅ React + TypeScript (via Vite)
- ✅ Tailwind CSS 3.4.1 with shadcn/ui theming system
- ✅ Path aliases (`@/`) configured
- ✅ 40+ shadcn/ui components pre-installed
- ✅ All Radix UI dependencies included
- ✅ Parcel configured for bundling (via .parcelrc)
- ✅ Node 18+ compatibility (auto-detects and pins Vite version)

### Step 2: Develop Your Artifact

To build the artifact, edit the generated files. See **Common Development Tasks** below for guidance.

### Step 3: Bundle to Single HTML File

To bundle the React app into a single HTML artifact:
```bash
bash scripts/bundle-artifact.sh
```

This creates `bundle.html` - a self-contained artifact with all JavaScript, CSS, and dependencies inlined. This file can be directly shared in Claude conversations as an artifact.

**Requirements**: Your project must have an `index.html` in the root directory.

**What the script does**:
- Installs bundling dependencies (parcel, @parcel/config-default, parcel-resolver-tspaths, html-inline)
- Creates `.parcelrc` config with path alias support
- Builds with Parcel (no source maps)
- Inlines all assets into single HTML using html-inline

### Step 4: Share Artifact with User

Finally, share the bundled HTML file in conversation with the user so they can view it as an artifact.

### Step 5: Testing/Visualizing the Artifact (Optional)

Note: This is a completely optional step. Only perform if necessary or requested.

To test/visualize the artifact, use available tools (including other Skills or built-in tools like Playwright or Puppeteer). In general, avoid testing the artifact upfront as it adds latency between the request and when the finished artifact can be seen. Test later, after presenting the artifact, if requested or if issues arise.

## Reference

- **shadcn/ui components**: https://ui.shadcn.com/docs/components