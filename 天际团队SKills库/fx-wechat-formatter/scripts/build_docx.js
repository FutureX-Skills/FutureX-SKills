#!/usr/bin/env node
/**
 * fx-wechat-formatter — 天际创意排版构建脚本
 * 用法: node build_docx.js <input.md> <palette> <output.docx>
 *   palette ∈ amber | sage | ember | frost
 *
 * 输入 markdown 方言:
 *   # 标题行                     可连续多行 #,放最前
 *   @series 主标签 | 副标签      眉头行(可选,紧跟标题下方,自动带强调色底线)
 *   ## 章节标题                  自动编号 01 02 03...
 *   > 金句                       金句引块(暖底+左边线)
 *   @readout 大字 | 小注         仪表读数(居中大字+灰色小注,小注可省略)
 *   @readout! 大字 | 小注        特大读数(28pt,用于单个数字如 27%)
 *   @cta                         CTA 色块开始,后续连续非空行进入色块,
 *                                首行为色块标题,空行结束
 *   [[文字]]                     正文内强调(强调色加粗)
 *   ---                          忽略
 *   其余非空行                    正文段落
 */
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  WidthType, ShadingType, AlignmentType, BorderStyle
} = require("docx");
const fs = require("fs");
const path = require("path");

// ---------- 配色 ----------
const PALETTES = {
  amber: { // 琥珀:深空蓝×电表琥珀。数据分析、投资框架、口径拆解类
    ink: "3A3F45", gray: "8A93A3", primary: "0F2540",
    accent: "E8930C", accent2: "F5A623", quoteFill: "FBF3E4"
  },
  sage: { // 青金:深松绿×古金。长文观察、政策解读、长期视角类
    ink: "3A3B36", gray: "8F8F82", primary: "1F3A2E",
    accent: "B8862B", accent2: "D9AF52", quoteFill: "F5F0E1"
  },
  ember: { // 炭橙:石墨黑×火橙。案例研究、创业故事、portfolio 深访类
    ink: "2E2E32", gray: "8F8F94", primary: "1A1A1E",
    accent: "D8532A", accent2: "E8724A", quoteFill: "FBEDE4"
  },
  frost: { // 雾青:深钢青×湖蓝。硬科技、技术拆解、芯片/模型架构类
    ink: "35404B", gray: "8996A3", primary: "1E2F3E",
    accent: "2E7A8E", accent2: "4FA5B8", quoteFill: "E8F0F3"
  }
};

const FONTS = { ascii: "Arial", hAnsi: "Arial", eastAsia: "微软雅黑" };
const PAGEW = 9360;

// ---------- CLI ----------
const [,, inputPath, paletteName, outputPath] = process.argv;
if (!inputPath || !paletteName || !outputPath) {
  console.error("用法: node build_docx.js <input.md> <amber|sage|ember|frost> <output.docx>");
  process.exit(1);
}
const p = PALETTES[paletteName];
if (!p) { console.error("未知配色: " + paletteName); process.exit(1); }
const src = fs.readFileSync(inputPath, "utf8");

// ---------- 组件 ----------
const run = (text, opts = {}) => new TextRun({ text, font: FONTS, size: 22, color: p.ink, ...opts });

function inlineRuns(text, baseOpts = {}) {
  const runs = [];
  text.split(/(\[\[.*?\]\])/).forEach(seg => {
    if (!seg) return;
    if (seg.startsWith("[[") && seg.endsWith("]]")) {
      runs.push(run(seg.slice(2, -2), { bold: true, color: p.accent, ...baseOpts }));
    } else {
      runs.push(run(seg, baseOpts));
    }
  });
  return runs;
}

const bodyPara = (text) => new Paragraph({
  children: inlineRuns(text),
  spacing: { after: 260, line: 380, lineRule: "auto" }
});

const h2 = (num, text) => new Paragraph({
  children: [
    run(num + "  ", { bold: true, color: p.accent, size: 30 }),
    run(text, { bold: true, color: p.primary, size: 30 })
  ],
  spacing: { before: 560, after: 300 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 10, color: p.accent, space: 6 } }
});

function readout(big, caption, size) {
  const out = [new Paragraph({
    children: [run(big, { bold: true, color: p.accent2, size })],
    alignment: AlignmentType.CENTER,
    spacing: { before: 300, after: caption ? 60 : 300 }
  })];
  if (caption) out.push(new Paragraph({
    children: [run(caption, { color: p.gray, size: 17 })],
    alignment: AlignmentType.CENTER,
    spacing: { after: 300 }
  }));
  return out;
}

const NONE = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };

const quoteBlock = (text) => new Table({
  width: { size: PAGEW, type: WidthType.DXA },
  columnWidths: [PAGEW],
  rows: [new TableRow({
    children: [new TableCell({
      width: { size: PAGEW, type: WidthType.DXA },
      shading: { type: ShadingType.CLEAR, fill: p.quoteFill },
      borders: { left: { style: BorderStyle.SINGLE, size: 28, color: p.accent }, top: NONE, bottom: NONE, right: NONE },
      margins: { top: 130, bottom: 130, left: 220, right: 180 },
      children: [new Paragraph({
        children: inlineRuns(text, { bold: true, color: p.primary, size: 24 }),
        spacing: { line: 360, lineRule: "auto" }
      })]
    })]
  })]
});

const CTA_GRAY = "595959"; // 深灰色,不随配色变化

function ctaBlock(lines) {
  const out = [new Paragraph({
    children: [],
    border: { top: { style: BorderStyle.SINGLE, size: 6, color: p.gray, space: 10 } },
    spacing: { before: 0, after: 200 }
  })];
  lines.forEach((line, i) => {
    out.push(new Paragraph({
      children: [run(line, { bold: true, color: CTA_GRAY, size: 20 })],
      spacing: { after: i === lines.length - 1 ? 0 : 100, line: 320, lineRule: "auto" }
    }));
  });
  return out;
}

const spacer = (h = 200) => new Paragraph({ children: [], spacing: { after: h } });

// ---------- 解析 ----------
const lines = src.split(/\r?\n/);
const children = [];
let sectionCount = 0;
let titleLines = [];   // 收集连续 # 行
let i = 0;

function flushTitle() {
  if (!titleLines.length) return;
  titleLines.forEach((t, idx) => {
    const last = idx === titleLines.length - 1;
    children.push(new Paragraph({
      children: [run(t, { bold: true, color: p.primary, size: 44 })],
      spacing: { after: last ? 140 : 40, line: 300, lineRule: "auto" }
    }));
  });
  children.push(spacer(120));
  titleLines = [];
}

while (i < lines.length) {
  const raw = lines[i];
  const line = raw.trim();
  i++;

  if (!line || line === "---") { flushTitle(); continue; }

  if (line.startsWith("@series ")) {
    flushTitle();
    const [main, sub] = line.slice(8).split("|").map(s => s.trim());
    const runs = [run(main, { bold: true, color: p.accent, size: 20 })];
    if (sub) runs.push(run("   " + sub, { color: p.gray, size: 16 }));
    children.push(new Paragraph({
      children: runs,
      spacing: { after: 240 },
      border: { bottom: { style: BorderStyle.SINGLE, size: 18, color: p.accent, space: 10 } }
    }));
    continue;
  }

  if (line.startsWith("# ") && !line.startsWith("## ")) {
    titleLines.push(line.slice(2).trim());
    continue;
  }
  flushTitle();

  if (line.startsWith("## ")) {
    sectionCount++;
    children.push(h2(String(sectionCount).padStart(2, "0"), line.slice(3).trim()));
    continue;
  }

  if (line.startsWith("> ")) {
    children.push(quoteBlock(line.slice(2).trim()));
    children.push(spacer());
    continue;
  }

  if (line.startsWith("@readout")) {
    const big = line.startsWith("@readout!");
    const rest = line.slice(big ? 9 : 8).trim();
    const [num, caption] = rest.split("|").map(s => s && s.trim());
    children.push(...readout(num, caption, big ? 56 : 32));
    continue;
  }

  if (line === "@cta") {
    const ctaLines = [];
    while (i < lines.length && lines[i].trim()) { ctaLines.push(lines[i].trim()); i++; }
    if (ctaLines.length) { children.push(spacer(200)); children.push(...ctaBlock(ctaLines)); }
    continue;
  }

  children.push(bodyPara(line));
}
flushTitle();

// ---------- 输出 ----------
const doc = new Document({
  styles: { default: { document: { run: { font: FONTS, size: 22, color: p.ink } } } },
  sections: [{
    properties: { page: { margin: { top: 1200, bottom: 1200, left: 1440, right: 1440 } } },
    children
  }]
});

Packer.toBuffer(doc).then(buf => {
  fs.mkdirSync(path.dirname(outputPath), { recursive: true });
  fs.writeFileSync(outputPath, buf);
  console.log("已生成:", outputPath, "(" + buf.length + " bytes, 配色: " + paletteName + ")");
});
