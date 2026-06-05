---
name: wechat-formatter
description: >
  Formats articles into WeChat Official Account (微信公众号) ready .docx files.
  Use whenever the user wants to format an article for WeChat, or says "排版", "生成公众号文章",
  "转换成公众号格式", "帮我排一下", "做成公众号" or similar.
  Output is a .docx file. User opens in Word, selects all (Ctrl+A), copies, pastes into WeChat editor.
  This is the ONLY reliable method — HTML paste is broken by WeChat's sanitizer.
---

# 微信公众号排版 Skill — DOCX 输出

## 工作流程

```
用户发来文章
    ↓
Claude 分析结构（章节 / 金句 / 关键词 / 关键数字）
    ↓
Claude 用 docx.js 生成 .docx 文件
    ↓
用户在 Word 里全选 → 复制 → 粘贴进微信公众号编辑器
```

**为什么用 docx 而不是 HTML？**
微信编辑器粘贴时会过滤掉所有 `<style>` 标签和 `class` 属性，导致 HTML 排版完全失效。
Word 的富文本格式粘贴进微信是完整保留的，这是目前唯一可靠的方案。

---

## 排版分析（生成代码前先做）

1. **章节划分** — 3~5 个逻辑段落，各配编号标题（01 / 02 / 03…）
2. **金句** — 提炼 1~3 句独立金句，用金句块处理
3. **重点段落** — 1~2 段最核心的分析，用重点段落块
4. **关键词** — 4~8 个专业词，用黄底 highlight 标注
5. **关键数字** — 重要数据/日期，用 ACCENT 色下划线（`underlined()` 函数）
6. **导读** — 写一句核心问题 + 2~3 句摘要
7. **阅读时长** — 中文字数 ÷ 400 ≈ 分钟数

---

## 配色系统

### 第一步：选择配色方案

**每次排版开始时，必须先询问用户选择配色方案**（除非用户已在消息中指定）：

> 请问这篇文章想用哪套配色方案？
> 1. **Wood** — 暖榛木色，沉稳知性（默认）
> 2. **Ink** — 纯黑白，极简有力
> 3. **Ocean** — 科技感深蓝，专业冷静
> 4. **Vermilion** — 中国红，传统与现代融合
> 5. **Mist** — 低饱和灰调，温柔克制
> 6. **Forest** — 墨绿自然，沉稳内敛
> 7. **Violet** — 深紫神秘，高端质感
> 8. **Amber** — 琥珀暖橙，活力温暖
>
> 或者上传文章封面图，我来自动匹配最适合的方案 🎨

**如果用户上传了封面图：** 见下方「封面图自动配色」章节。

---

### 8 套配色方案定义

每套方案包含 6 个变量，直接替换脚本中的对应色值即可。
`ACCENT` = 主强调色（左边框/装饰线），`ACCENT2` = 次强调色（金句边框），
`DARK` = 深色文字，`SMOKE` = 正文，`DUST` = 次要文字，`TITAN` = 最淡文字，
`BORDER_LIGHT` = 分隔线，`HIGHLIGHT_BG` = 关键词底色（Word highlight 用内置色名）

```javascript
// ━━ 1. Wood（默认）━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
const ACCENT       = "C4A882"   // 木色 — 左边框 / 装饰线 / 下划线
const ACCENT2      = "B89860"   // 金色 — 金句左边框
const DARK         = "2E2E2E"
const SMOKE        = "4A4845"
const DUST         = "8A8480"
const TITAN        = "B8B4AE"
const BORDER_LIGHT = "ECEAE5"
const ACCENT_BORDER= "F0EBE0"   // 金句上下细线
// highlight: "yellow"

// ━━ 2. Ink ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
const ACCENT       = "111111"
const ACCENT2      = "555555"
const DARK         = "111111"
const SMOKE        = "333333"
const DUST         = "666666"
const TITAN        = "999999"
const BORDER_LIGHT = "E0E0E0"
const ACCENT_BORDER= "F0F0F0"
// highlight: "darkGray"  ← Word 内置色，灰底黑字

// ━━ 3. Ocean ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
const ACCENT       = "2A6DB5"
const ACCENT2      = "5A8AB8"
const DARK         = "0D2D4A"
const SMOKE        = "2A4560"
const DUST         = "5A8AB8"
const TITAN        = "8AAAC8"
const BORDER_LIGHT = "D0E0F0"
const ACCENT_BORDER= "DCE9F7"
// highlight: "cyan"

// ━━ 4. Vermilion ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
const ACCENT       = "C03A1A"
const ACCENT2      = "A05040"
const DARK         = "2A0A06"
const SMOKE        = "3D2018"
const DUST         = "A05040"
const TITAN        = "C09080"
const BORDER_LIGHT = "F0DDD8"
const ACCENT_BORDER= "F9E8E3"
// highlight: "red"

// ━━ 5. Mist ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
const ACCENT       = "A09888"
const ACCENT2      = "7A7468"
const DARK         = "2C2820"
const SMOKE        = "4A4438"
const DUST         = "8C8478"
const TITAN        = "B4AFA8"
const BORDER_LIGHT = "E0DBD4"
const ACCENT_BORDER= "EDE8E0"
// highlight: "darkGray"

// ━━ 6. Forest ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
const ACCENT       = "2A7A48"
const ACCENT2      = "4A8A62"
const DARK         = "0D2A18"
const SMOKE        = "1E3A28"
const DUST         = "4A8A62"
const TITAN        = "80AA90"
const BORDER_LIGHT = "C8E8D4"
const ACCENT_BORDER= "D8EDE0"
// highlight: "green"

// ━━ 7. Violet ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
const ACCENT       = "6A3DB8"
const ACCENT2      = "8A6AC0"
const DARK         = "1A0A35"
const SMOKE        = "2A1250"
const DUST         = "8A6AC0"
const TITAN        = "A898D8"
const BORDER_LIGHT = "DDD4F4"
const ACCENT_BORDER= "EAE3F8"
// highlight: "darkMagenta"

// ━━ 8. Amber ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
const ACCENT       = "D4860A"
const ACCENT2      = "B87820"
const DARK         = "251500"
const SMOKE        = "3A2800"
const DUST         = "B87820"
const TITAN        = "C8A060"
const BORDER_LIGHT = "F0DCA8"
const ACCENT_BORDER= "FAECC8"
// highlight: "yellow"
```

> 📌 **使用方法**：将选定方案的色值粘贴到脚本顶部，替换默认的 Wood 方案。
> 所有组件库中的 `WOOD`、`GOLD` 统一改为 `ACCENT`、`ACCENT2`，其余变量名不变。

---

### 封面图自动配色

**当用户上传封面图时，执行以下流程：**

**Step 1 — 提取主色调**
用肉眼（或 Claude 视觉能力）判断封面图的主色相：
- 偏暖棕/米色 → Wood
- 接近纯黑白/灰 → Ink
- 深蓝/青色调 → Ocean
- 红色/朱砂/橙红 → Vermilion
- 中低饱和暖灰/米 → Mist
- 绿色/深绿 → Forest
- 紫色/靛色 → Violet
- 橙色/金黄 → Amber

**Step 2 — 匹配度判断**
如果封面图主色与某套方案相似度较高（同色相、饱和度相近），**直接使用预设方案**，并告知用户：
> 根据封面图，推荐使用「Ocean」方案，是否确认？

**Step 3 — 匹配度低时，生成定制配色**
如果封面图色彩独特（如品牌色、特殊摄影调色），预设方案无法贴近，则提取封面图主色自动生成定制方案：

```javascript
// 定制方案生成规则（从封面图主色 HEX 推导）
// 设封面图提取到主色为 BASE_HEX（如 "3D7A8A"）

ACCENT        = BASE_HEX                   // 直接用主色做边框/装饰
ACCENT2       = BASE_HEX 亮度 +15%         // 略亮版做次要强调
DARK          = "1A1A1A"                   // 深色文字固定不变
SMOKE         = "383838"                   // 正文固定不变
DUST          = BASE_HEX 饱和度 -30% +灰   // 主色去饱和版做次要文字
TITAN         = BASE_HEX 亮度 +40% +灰    // 极淡版做最次要文字
BORDER_LIGHT  = BASE_HEX 亮度 +55%        // 非常淡，做分隔线
ACCENT_BORDER = BASE_HEX 亮度 +60%        // 最淡，做金句边框底色
// 背景始终保持白色（FFFFFF），不跟随主色变化
// highlight 根据主色色相选最接近的 Word 内置色
```

> ⚠️ **背景始终白色**：定制配色只调整 ACCENT/ACCENT2/DUST/TITAN，深色文字（DARK/SMOKE）固定为近黑，背景不跟随主色染色，确保公众号阅读体验。

---

## 技术要点（必读，避免踩坑）

```javascript
// 安装
npm install docx

// 引入
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
        AlignmentType, BorderStyle, WidthType, ShadingType, VerticalAlign,
        TableLayoutType, LevelFormat } = require('docx');

// 输出
Packer.toBuffer(doc).then(buf => fs.writeFileSync('output.docx', buf));
```

**关键约束：**
- 所有表格必须同时设置 `columnWidths`（表级）和每个 cell 的 `width`，两者必须一致
- 单位统一用 DXA（1440 DXA = 1 英寸）。A4 内容宽：11906 - 2880 = **9026 DXA**
- `ShadingType.CLEAR` 不是 `SOLID`（SOLID 会出现黑色背景）
- ⚠️ Hero / Footer **禁止用 shading**（见 Hero 块设计原则），改用左竖线 + 纯色文字
- **JS 字符串里的中文引号 `"…"` 必须转义**，用 `\u201c` / `\u201d`，否则 SyntaxError
- 文字内不用 `\n`，换行用独立的 `new Paragraph()`
- `border` 属性中不用的方向设为 `{ style: BorderStyle.NONE, size: 0, color: "FFFFFF" }`

---

## 完整组件库

### 基础 helper 函数（每次都复制进脚本）

```javascript
const noBorder = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
const noBorders = { top: noBorder, bottom: noBorder, left: noBorder, right: noBorder };
const hairline  = (c) => ({ style: BorderStyle.SINGLE, size: 1, color: c });

function sp(before = 0, after = 0) {
  return { spacing: { before, after } };
}

// 关键词高亮 — highlight 色跟随方案（见配色方案定义中的 // highlight: 注释）
// 生成脚本时将 "yellow" 替换为当前方案对应的 Word highlight 色名
function tagged(text) {
  return new TextRun({ text, highlight: "yellow", bold: true, size: 25 }); // ← 按方案替换色名
}

// 关键数字（wood 下划线）
function underlined(text) {
  return new TextRun({ text, color: DARK, bold: true, underline: { color: ACCENT } });
}

// 章节间留白（导读→章节、章节→章节之间用空段落留白，不用横线）
// 线只保留在章节标题下方（见章节标题组件的 border.bottom）
function gap() {
  return new Paragraph({ ...sp(480, 0) });
}

// wood 左边框（重点段落）
function woodBorder() {
  return {
    left:   { style: BorderStyle.SINGLE, size: 24, color: ACCENT, space: 12 },
    top:    noBorder, bottom: noBorder, right: noBorder
  };
}

// gold 左边框 + 上下细线（金句）
function goldBorder() {
  return {
    left:   { style: BorderStyle.SINGLE, size: 18, color: ACCENT2, space: 12 },
    top:    { style: BorderStyle.SINGLE, size: 2,  color: ACCENT_BORDER },
    bottom: { style: BorderStyle.SINGLE, size: 2,  color: ACCENT_BORDER },
    right:  noBorder
  };
}
```

---

### HERO 块

**设计原则：主标题裸排不加任何背景，副信息用左竖线统一成一个视觉块，避免微信里出现一块块割裂的深色色块。**

```javascript
// ── 主标题：纯文字，无背景，无边框 ──
new Paragraph({
  children: [new TextRun({ text: "{{大标题}}", color: DARK, bold: true, size: 52, font: "PingFang SC" })],
  ...sp(240, 160)
}),
// ── 副标题（如有）：灰色中字，无背景 ──
new Paragraph({
  children: [new TextRun({ text: "{{副标题}}", color: SMOKE, size: 24, font: "PingFang TC" })],
  ...sp(0, 200)
}),

// ── META 块：用 wood 左竖线统一三行信息，不用 shading ──
// 第一行：话题标签 · 来源
new Paragraph({
  children: [
    new TextRun({ text: "{{话题标签}}  ·  FutureX Capital  天际资本", color: DUST, size: 20, characterSpacing: 100 })
  ],
  border: { left: { style: BorderStyle.SINGLE, size: 16, color: ACCENT, space: 10 }, top: noBorder, bottom: noBorder, right: noBorder },
  indent: { left: 200 },
  ...sp(0, 80)
}),
// 第二行：活动类型 · 嘉宾信息
new Paragraph({
  children: [
    new TextRun({ text: "{{活动类型}}  ·  {{嘉宾信息}}", color: SMOKE, size: 22 })
  ],
  border: { left: { style: BorderStyle.SINGLE, size: 16, color: ACCENT, space: 10 }, top: noBorder, bottom: noBorder, right: noBorder },
  indent: { left: 200 },
  ...sp(0, 80)
}),
// 第三行：日期 · 预计阅读时长
new Paragraph({
  children: [
    new TextRun({ text: "{{日期}}  ·  预计阅读 {{N}} 分钟", color: TITAN, size: 20 })
  ],
  border: { left: { style: BorderStyle.SINGLE, size: 16, color: ACCENT, space: 10 }, top: noBorder, bottom: noBorder, right: noBorder },
  indent: { left: 200 },
  ...sp(0, 320)
}),
```

> ⚠️ **不要用 `shading`**：shading 每行独立渲染，微信粘贴后行间会出现白缝，变成一块块割裂色块。统一用左竖线方案，整体感更好。

---

### 导读块

```javascript
// 导读标签
new Paragraph({
  children: [new TextRun({ text: "导  读", color: ACCENT, bold: true, size: 20, characterSpacing: 160 })],
  ...sp(320, 80)
}),
// 核心问题（大字）
new Paragraph({
  children: [new TextRun({ text: "{{核心问题}}", color: DARK, bold: true, size: 32, font: "PingFang SC" })],
  ...sp(0, 80)
}),
// 摘要（wood 左边框）
new Paragraph({
  children: [new TextRun({ text: "{{摘要内容}}", color: SMOKE, size: 24, font: "PingFang TC" })],
  border: woodBorder(),
  indent: { left: 240 },
  ...sp(0, 320)
}),
```

---

### 章节标题（编号 + 标题）

```javascript
// 章节编号（wood 色斜体大字）
new Paragraph({
  children: [new TextRun({ text: "01", color: ACCENT, size: 52, font: "Georgia", italics: true })],
  ...sp(320, 80)
}),
// 章节标题（带底部细线 — 全文唯一横分割线）
new Paragraph({
  children: [new TextRun({ text: "{{章节标题}}", color: DARK, bold: true, size: 34, font: "PingFang SC" })],
  border: { bottom: { style: BorderStyle.SINGLE, size: 2, color: BORDER_LIGHT, space: 4 } },
  ...sp(0, 200)
}),
```

---

### 正文段落

```javascript
new Paragraph({
  children: [
    new TextRun({ text: "正文内容，可以穿插 ", color: SMOKE, size: 24 }),
    tagged("关键词"),
    new TextRun({ text: " 和 ", color: SMOKE, size: 24 }),
    underlined("关键数字"),
    new TextRun({ text: " 在段落中。", color: SMOKE, size: 24 }),
  ],
  ...sp(0, 160)
}),
```

---

### 金句块

```javascript
new Paragraph({
  children: [new TextRun({ text: "{{金句内容}}", color: DARK, size: 24, font: "PingFang TC" })],
  border: goldBorder(),
  indent: { left: 360 },
  ...sp(160, 80)
}),
new Paragraph({
  children: [new TextRun({ text: "{{来源/作者}}", color: TITAN, size: 20 })],
  border: { left: { style: BorderStyle.SINGLE, size: 18, color: ACCENT2, space: 12 }, top: noBorder, bottom: noBorder, right: noBorder },
  indent: { left: 360 },
  ...sp(0, 240)
}),
```

---

### 重点段落

```javascript
new Paragraph({
  children: [new TextRun({ text: "{{重点内容}}", color: DARK, size: 24, font: "PingFang TC" })],
  border: woodBorder(),
  indent: { left: 360 },
  ...sp(80, 240)
}),
```

---

### 三栏概念表（Models / Apps / Harnesses 类）

```javascript
// colW * 3 = 9026（A4 内容宽）约取 2920 * 3 = 8760，左右各留 133
new Table({
  width: { size: 8760, type: WidthType.DXA },
  columnWidths: [2920, 2920, 2920],
  layout: TableLayoutType.FIXED,
  rows: [
    // 表头行
    new TableRow({ children: [
      new TableCell({
        borders: { top: noBorder, bottom: { style: BorderStyle.SINGLE, size: 8, color: DARK }, left: noBorder, right: noBorder },
        width: { size: 2920, type: WidthType.DXA },
        margins: { top: 0, bottom: 80, left: 0, right: 120 },
        children: [new Paragraph({ children: [new TextRun({ text: "LABEL_1", color: DUST, size: 18, bold: true, characterSpacing: 80 })] })]
      }),
      // 同结构，第2/3列加 left: hairline(BORDER_LIGHT)
    ]}),
    // 内容行
    new TableRow({ children: [
      new TableCell({
        borders: { top: noBorder, bottom: hairline(BORDER_LIGHT), left: noBorder, right: noBorder },
        width: { size: 2920, type: WidthType.DXA },
        margins: { top: 80, bottom: 80, left: 0, right: 120 },
        children: [
          new Paragraph({ children: [new TextRun({ text: "中文标题", color: DARK, bold: true, size: 26 })], spacing: { after: 40 } }),
          new Paragraph({ children: [new TextRun({ text: "描述内容", color: DUST, size: 22 })], spacing: { after: 0 } })
        ]
      }),
      // 同结构，第2/3列 left: hairline(BORDER_LIGHT)
    ]})
  ]
})
```

---

### 两列工具/要点表

```javascript
// 左列宽 1600，右列宽 7160，合计 8760
new Table({
  width: { size: 8760, type: WidthType.DXA },
  columnWidths: [1600, 7160],
  layout: TableLayoutType.FIXED,
  rows: [
    new TableRow({ children: [
      new TableCell({
        borders: { top: hairline(BORDER_LIGHT), bottom: noBorder, left: noBorder, right: hairline(BORDER_LIGHT) },
        width: { size: 1600, type: WidthType.DXA },
        margins: { top: 120, bottom: 120, left: 0, right: 120 },
        verticalAlign: VerticalAlign.TOP,
        children: [
          new Paragraph({ children: [new TextRun({ text: "名称", color: DARK, bold: true, size: 24 })] }),
          new Paragraph({ children: [new TextRun({ text: "标签", color: ACCENT, size: 18 })], spacing: { before: 40 } })
        ]
      }),
      new TableCell({
        borders: { top: hairline(BORDER_LIGHT), bottom: noBorder, left: noBorder, right: noBorder },
        width: { size: 7160, type: WidthType.DXA },
        margins: { top: 120, bottom: 120, left: 160, right: 0 },
        children: [new Paragraph({ children: [new TextRun({ text: "描述内容", color: SMOKE, size: 24 })], spacing: { after: 0 } })]
      })
    ]})
    // 每条目重复一个 TableRow
  ]
})
```

---

### 来源注释

```javascript
new Paragraph({
  children: [new TextRun({ text: "原文 · {{作者}}  /  {{来源}}  /  {{日期}}", color: TITAN, size: 22 })],
  border: { top: { style: BorderStyle.SINGLE, size: 2, color: BORDER_LIGHT, space: 4 } },
  ...sp(160, 480)
}),
```

---

### FOOTER 块

**不用 shading，改用顶部 wood 色粗线 + 灰色文字，干净有品。**

```javascript
new Paragraph({
  children: [new TextRun({ text: "FutureX Capital  天际资本  ·  AI 前沿", color: DUST, size: 20, characterSpacing: 80 })],
  border: { top: { style: BorderStyle.SINGLE, size: 12, color: ACCENT, space: 8 }, bottom: noBorder, left: noBorder, right: noBorder },
  ...sp(320, 160)
}),
new Paragraph({
  children: [new TextRun({ text: "转载请注明来源", color: TITAN, size: 18 })],
  ...sp(0, 480)
}),
```

---

## 完整脚本骨架

```javascript
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
        AlignmentType, BorderStyle, WidthType, ShadingType, VerticalAlign,
        TableLayoutType } = require('docx');
const fs = require('fs');

// ── 配色 ──────────────────────────────────────────────────
// ── 色值从上方"配色方案定义"章节复制到此处 ──
const ACCENT = "C4A882", ACCENT2 = "B89860", DARK = "2E2E2E", SMOKE = "4A4845";
const DUST = "8A8480", TITAN = "B8B4AE", WHITE = "FFFFFF";
const BORDER_LIGHT = "ECEAE5", ACCENT_BORDER = "F0EBE0";

// ── Helpers ───────────────────────────────────────────────
const noBorder = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
const hairline  = (c) => ({ style: BorderStyle.SINGLE, size: 1, color: c });
const sp = (before, after) => ({ spacing: { before, after } });
const tagged    = (text) => new TextRun({ text, highlight: "yellow", bold: true, size: 25 }); // ← 按方案替换色名
const underlined= (text) => new TextRun({ text, color: DARK, bold: true, underline: { color: ACCENT } });
function gap() {
  return new Paragraph({ ...sp(480, 0) });
}
function woodBorder() {
  return { left: { style: BorderStyle.SINGLE, size: 24, color: ACCENT, space: 12 }, top: noBorder, bottom: noBorder, right: noBorder };
}
function goldBorder() {
  return { left: { style: BorderStyle.SINGLE, size: 18, color: ACCENT2, space: 12 },
           top: { style: BorderStyle.SINGLE, size: 2, color: ACCENT_BORDER },
           bottom: { style: BorderStyle.SINGLE, size: 2, color: ACCENT_BORDER }, right: noBorder };
}

// ── 文档 ──────────────────────────────────────────────────
const doc = new Document({
  styles: {
    default: { document: { run: { font: "PingFang TC", size: 24, color: SMOKE } } }
  },
  sections: [{
    properties: {
      page: {
        size: { width: 11906, height: 16838 },           // A4
        margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 }
      }
    },
    children: [
      // ── HERO ──
      // ── 导读 ──
      // gap()
      // ── 章节 01 ──
      // gap(), sectionNumber, sectionTitle, bodyPara...
      // ── FOOTER ──
    ]
  }]
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync('/mnt/user-data/outputs/article.docx', buf);
  console.log('Done');
});
```

> ⚠️ **中文引号转义**：JS 字符串中的 `"` 和 `"` 必须写成 `\u201c` / `\u201d`，否则会 SyntaxError。
> 用这个 Python 一键修复：
> ```python
> python3 -c "
> import re
> with open('script.js','r') as f: c=f.read()
> # escape embedded double-quotes inside JS string literals
> # ... (see build_article.js 中的修复逻辑)
> "
> ```
> 更简单：直接把含中文引号的文本改用角括号 `「」` 替代 `""`。

---

## 质量核查

- [ ] **已询问/确认配色方案**，脚本顶部色值已替换为对应方案
- [ ] 如有封面图：已完成匹配或定制配色流程
- [ ] `npm install docx` 已安装
- [ ] 所有表格：`columnWidths` 之和 = `width.size`，且每个 cell 的 `width` 与列宽一致
- [ ] 所有 shading 用 `ShadingType.CLEAR`（不是 SOLID）
- [ ] ⚠️ **Hero / Footer 禁止用 shading**：会在微信粘贴时产生行间白缝，一块块很丑；改用左竖线 + 纯色文字方案
- [ ] JS 字符串中无裸 `"` / `"` 中文引号（已转义或改用 `「」`）
- [ ] 有 1~3 个金句块（goldBorder）
- [ ] 有重点段落（woodBorder）
- [ ] 关键词用 `highlight` — 色名已按方案替换（Wood/Amber→yellow，Ink/Mist→darkGray，Ocean→cyan，Vermilion→red，Forest→green，Violet→darkMagenta）
- [ ] 关键数字用 `underline: { color: ACCENT }`
- [ ] 输出路径：`/mnt/user-data/outputs/文件名.docx`
- [ ] 运行 `node script.js` 输出 `Done` 无报错
