---
name: pptx-logo-label-fix
description: >
  Use this skill whenever the user has a PowerPoint (.pptx) file where
  company logos and their text labels need to be matched, fixed, or updated —
  regardless of whether the companies are known in advance. This covers:
  logos with wrong category labels underneath them, empty text boxes below
  logos, labels that got scrambled after slides were rearranged, adding
  Chinese descriptions to English company names, or any request like "the
  labels don't match the logos", "fix the ribbon companies", "missed this
  segment", "wrong category under this logo", or "update the portfolio slide".
  Works for FutureX decks and any other PPTX portfolio/map slide. Always use
  this skill when the task involves identifying companies from logo images and
  correcting or adding text labels beneath them.
---

# PPTX Logo–Label Fix

## The Core Problem This Skill Solves

Portfolio slides often have logo images and text labels arranged in groups.
When slides get rearranged in PowerPoint, the labels underneath logos get
scrambled — wrong descriptions end up under wrong companies, or labels go
missing entirely. The fix requires three things working together:

1. **Seeing** — visually extracting and identifying each logo
2. **Knowing** — determining the correct label for each company
3. **Editing safely** — modifying the PPTX XML without corrupting it

This skill teaches all three.

---

## Step 1: Load and Explore the File

PPTX files are ZIP archives. Load everything from the ZIP upfront so you can
work efficiently without repeated reads:

```python
import zipfile, re, io, os

pptx_path = '/path/to/input.pptx'

with zipfile.ZipFile(pptx_path, 'r') as z:
    all_files = {name: z.read(name) for name in z.namelist()}
    namelist = z.namelist()

# The slide you'll be editing (adjust slide number as needed)
slide_key = 'ppt/slides/slide21.xml'
slide_xml = all_files[slide_key].decode('utf-8')

# Relationship file maps rId codes → actual image files
rels_key = f'ppt/slides/_rels/slide21.xml.rels'
rels_xml = all_files[rels_key].decode('utf-8')

# Build a lookup: rId → image path inside the ZIP
rids = {}
for m in re.finditer(r'Id="(rId\d+)"[^>]*Target="([^"]+\.(?:png|PNG|jpg|jpeg))"', rels_xml):
    rids[m.group(1)] = m.group(2).replace('../', 'ppt/')
```

---

## Step 2: Find All Logo Groups and Extract Images

The slide's logos are inside `<p:grpSp>` (group shape) elements. Each group
typically contains one image (`<p:pic>`) and one text box (`<p:sp>`). Extract
every group and sort by x-position to get left-to-right order.

```python
def find_grpsp_end(xml, start):
    """Find the closing tag of a <p:grpSp> block, handling nesting."""
    depth, i = 0, start
    while i < len(xml):
        if xml[i:i+9] == '<p:grpSp>':
            depth += 1; i += 9
        elif xml[i:i+10] == '</p:grpSp>':
            depth -= 1
            if depth == 0:
                return i + 10
            i += 10
        else:
            i += 1
    return -1

def extract_groups(slide_xml, all_files, rids, output_dir):
    """
    Extract all shape groups from a slide, save their logo images,
    and return info about each group sorted left-to-right by x position.
    """
    os.makedirs(output_dir, exist_ok=True)
    groups = []
    i = 0
    while True:
        start = slide_xml.find('<p:grpSp>', i)
        if start == -1:
            break
        end = find_grpsp_end(slide_xml, start)
        if end == -1:
            break
        block = slide_xml[start:end]
        i = start + 1

        # Get this group's position
        xfrm = re.search(r'<a:xfrm><a:off x="(\d+)" y="(\d+)"', block)
        if not xfrm:
            continue
        x_pos, y_pos = int(xfrm.group(1)), int(xfrm.group(2))

        # Get all shape IDs in this group
        all_ids = re.findall(r'<p:cNvPr id="(\d+)"', block)

        # Get current text labels
        texts = [t for t in re.findall(r'<a:t>([^<]*)</a:t>', block) if t.strip()]

        # Find the text shape (sp) and its ID
        sp_shapes = []
        for sp_m in re.finditer(r'<p:sp>(.*?)</p:sp>', block, re.DOTALL):
            sp_block = sp_m.group(0)
            sp_id = re.search(r'<p:cNvPr id="(\d+)"', sp_block)
            sp_texts = re.findall(r'<a:t>([^<]*)</a:t>', sp_block)
            if sp_id:
                sp_shapes.append({'id': sp_id.group(1), 'texts': sp_texts})

        # Extract the logo image if present
        blip = re.search(r'r:embed="(rId\d+)"', block)
        logo_path = None
        if blip and blip.group(1) in rids:
            img_zip_path = rids[blip.group(1)]
            if img_zip_path in all_files:
                ext = img_zip_path.split('.')[-1]
                logo_path = f'{output_dir}/logo_x{x_pos}_y{y_pos}.{ext}'
                with open(logo_path, 'wb') as f:
                    f.write(all_files[img_zip_path])

        groups.append({
            'x': x_pos, 'y': y_pos,
            'all_ids': all_ids,
            'current_texts': texts,
            'sp_shapes': sp_shapes,
            'logo_path': logo_path,
        })

    # Sort: top row first (by y), then left-to-right (by x)
    groups.sort(key=lambda g: (g['y'], g['x']))
    return groups
```

**After running this**, use the `Read` tool on each extracted logo file to see
what company it is. You're doing visual identification — don't trust the
current text label, since fixing those mismatches is the whole point.

---

## Step 3: Identify Each Company

For each extracted logo image:

1. **Read it visually** — use the `Read` tool on the logo file
2. **Identify the company** from the logo design (name, icon, style)
3. **Determine the correct label** using this priority order:
   - If the company is in the **FutureX known list** below → use that label
   - If the company is new/unknown → look at what they do (web search if needed)
     and assign an appropriate Chinese category label
   - If you genuinely can't identify it → note the logo filename and ask the user

Build a change list: `[ (text_shape_id, "correct label"), ... ]`
Only include entries where the current label is wrong or missing.

### FutureX Known Companies (as of v13)

This is a cache, not a hard constraint. If a company has been added since
this list was written, identify it visually and assign a label based on what
it does. Use this as a reference, not the source of truth.

Read `references/futureX-companies.md` for the full company-to-label table.

---

## Step 4: Apply the Fixes Safely

**The most important rule in this entire skill:** Never use Python's
`ElementTree` or any XML parser to read and re-serialize PPTX XML. Parsers
rename namespace prefixes (e.g., `r:` becomes `ns2:`), which breaks the file
silently — the PPTX appears to open but images and formatting are corrupted.
Always edit the XML as a plain string using regex.

```python
def replace_text_in_shape(xml, shape_id, new_text):
    """
    Replace all text content in a shape with new_text.
    Handles multi-run text (where text is split across multiple <a:r> tags)
    by consolidating everything into a single run, preserving the original
    run's formatting properties.
    """
    m = re.search(rf'<p:cNvPr id="{shape_id}"[^>]*>', xml)
    if not m:
        return xml, False
    pos = m.start()

    # Walk backwards to find the enclosing shape element
    shape_start, shape_tag = None, None
    for tag in ['<p:sp>', '<p:grpSp>', '<p:pic>', '<p:graphicFrame>']:
        c = xml.rfind(tag, 0, pos)
        if c != -1:
            shape_start, shape_tag = c, tag
            break
    if shape_start is None:
        return xml, False

    close_tag = shape_tag.replace('<', '</')
    end = xml.find(close_tag, pos)
    block = xml[shape_start : end + len(close_tag)]

    # Find all text runs in this shape
    ar_matches = list(re.finditer(r'(<a:r>)(.*?)(</a:r>)', block, re.DOTALL))

    if not ar_matches:
        # Simple case: direct <a:t> tag with no run wrapper
        at = re.search(r'<a:t>[^<]*</a:t>', block)
        if at:
            new_block = block[:at.start()] + f'<a:t>{new_text}</a:t>' + block[at.end():]
        else:
            return xml, False
    else:
        # Multi-run case: grab formatting from first run, replace all runs with one
        rpr = re.search(r'(<a:rPr[^>]*/?>)', ar_matches[0].group(2))
        rpr_str = rpr.group(1) if rpr else ''
        new_run = f'<a:r>{rpr_str}<a:t>{new_text}</a:t></a:r>'
        new_block = block[:ar_matches[0].start()] + new_run + block[ar_matches[-1].end():]

    return xml[:shape_start] + new_block + xml[end + len(close_tag):], True


# Apply all changes
changes = [
    (shape_id_1, 'correct label 1'),
    (shape_id_2, 'correct label 2'),
    # ...
]

modified_xml = slide_xml
results = []
for shape_id, new_label in changes:
    modified_xml, ok = replace_text_in_shape(modified_xml, shape_id, new_label)
    results.append((shape_id, new_label, '✓' if ok else '✗ FAILED'))

for r in results:
    print(f"  id={r[0]} → '{r[1]}' {r[2]}")
```

---

## Step 5: Rebuild and Verify the PPTX

```python
# Determine output version number
import glob
existing = glob.glob('/path/to/outputs/FutureX_AGI_Fund_Chinese_v*.pptx')
versions = [int(re.search(r'v(\d+)', f).group(1)) for f in existing if re.search(r'v(\d+)', f)]
next_version = max(versions) + 1 if versions else 1
output_path = f'/path/to/outputs/FutureX_AGI_Fund_Chinese_v{next_version}.pptx'

# Build the new ZIP, replacing only the modified slide
out_buf = io.BytesIO()
with zipfile.ZipFile(out_buf, 'w', zipfile.ZIP_DEFLATED) as zout:
    for name in namelist:
        data = modified_xml.encode('utf-8') if name == slide_key else all_files[name]
        zout.writestr(name, data)

with open(output_path, 'wb') as f:
    f.write(out_buf.getvalue())

# Verify the output
with zipfile.ZipFile(output_path, 'r') as z:
    check = z.read(slide_key).decode('utf-8')
    file_count = len(z.namelist())

ns2_count = check.count('ns2:')
has_standalone = 'standalone="yes"' in check[:300]
print(f"✓ {file_count} files in ZIP")
print(f"{'✓' if ns2_count == 0 else '✗'} Namespace corruption: {ns2_count} ns2: instances")
print(f"{'✓' if has_standalone else '✗'} standalone='yes' declaration")

# Spot-check a few labels you just wrote
for label in [label for _, label, _ in results]:
    present = label in check
    print(f"  {'✓' if present else '✗'} '{label}'")
```

---

## Common Issues and Fixes

**"The output PPTX opens but looks broken / images missing"**
→ XML namespace corruption. Check for `ns2:` in the slide XML. If present,
the XML was parsed with ElementTree at some point. Redo using only string/regex.

**"My change list has the right labels but replace_text_in_shape returns False"**
→ The shape ID may have changed in this version of the deck. Use the
`extract_groups()` function above to re-discover IDs fresh from the file.

**"The label text is spread across multiple lines in the XML"**
→ Multi-run text — the function handles this automatically by consolidating
all `<a:r>` runs into one while preserving the first run's formatting.

**"There are 15 logos but I can only find 13 groups"**
→ Some groups may be nested inside a parent `<p:grpSp>`. The
`find_grpsp_end()` / depth-tracking approach above handles nesting correctly
as long as you don't stop at the first `</p:grpSp>` you find.

**"I can't identify a logo — it has no text and an abstract icon"**
→ Note the logo's filename and x/y position, then ask the user: "I see a logo
at position [N] from the left in the top row — can you tell me which company
this is?" Don't guess; get it right.

---

## Reference Files

- `references/futureX-companies.md` — Full FutureX portfolio company list with correct Chinese labels (as of v13). Use as a cache for known companies; don't treat it as exhaustive.
- `references/shape-id-discovery.md` — Script for systematically enumerating all groups and their shape IDs when working with a new or restructured deck version.
