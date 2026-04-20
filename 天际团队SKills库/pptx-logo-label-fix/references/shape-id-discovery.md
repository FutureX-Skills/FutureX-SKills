# Shape ID Discovery for New Deck Versions

When a new version of the deck has been edited in PowerPoint, shape IDs may
have shifted. Run this to rediscover which ID corresponds to which company.

```python
import zipfile, re, os

def discover_all_groups(pptx_path, slide_num=21, output_dir='/tmp/logos'):
    """
    Enumerate all shape groups in a slide, extract their logos,
    and print a summary for visual identification.
    """
    os.makedirs(output_dir, exist_ok=True)

    with zipfile.ZipFile(pptx_path, 'r') as z:
        all_files = {name: z.read(name) for name in z.namelist()}

    slide_key = f'ppt/slides/slide{slide_num}.xml'
    rels_key = f'ppt/slides/_rels/slide{slide_num}.xml.rels'
    slide_xml = all_files[slide_key].decode('utf-8')
    rels_xml = all_files[rels_key].decode('utf-8')

    rids = {}
    for m in re.finditer(r'Id="(rId\d+)"[^>]*Target="([^"]+\.(?:png|PNG|jpg|jpeg))"', rels_xml):
        rids[m.group(1)] = m.group(2).replace('../', 'ppt/')

    def find_end(xml, start):
        depth, i = 0, start
        while i < len(xml):
            if xml[i:i+9] == '<p:grpSp>': depth += 1; i += 9
            elif xml[i:i+10] == '</p:grpSp>':
                depth -= 1
                if depth == 0: return i + 10
                i += 10
            else: i += 1
        return -1

    groups = []
    i = 0
    while True:
        start = slide_xml.find('<p:grpSp>', i)
        if start == -1: break
        end = find_end(slide_xml, start)
        if end == -1: break
        block = slide_xml[start:end]
        i = start + 1

        xfrm = re.search(r'<a:xfrm><a:off x="(\d+)" y="(\d+)"', block)
        if not xfrm: continue
        x, y = int(xfrm.group(1)), int(xfrm.group(2))

        texts = [t.strip() for t in re.findall(r'<a:t>([^<]*)</a:t>', block) if t.strip()]

        sp_info = []
        for sp_m in re.finditer(r'<p:sp>(.*?)</p:sp>', block, re.DOTALL):
            sp = sp_m.group(0)
            sid = re.search(r'<p:cNvPr id="(\d+)"', sp)
            st = re.findall(r'<a:t>([^<]*)</a:t>', sp)
            if sid: sp_info.append(f"id={sid.group(1)}: {st}")

        blip = re.search(r'r:embed="(rId\d+)"', block)
        logo_saved = None
        if blip and blip.group(1) in rids:
            img = rids[blip.group(1)]
            if img in all_files:
                ext = img.split('.')[-1]
                logo_saved = f'{output_dir}/x{x}_y{y}.{ext}'
                with open(logo_saved, 'wb') as f:
                    f.write(all_files[img])

        groups.append((y, x, texts, sp_info, logo_saved))

    groups.sort()  # sort by (y, x) = top-to-bottom, left-to-right
    print(f"\nFound {len(groups)} groups in slide {slide_num}:\n")
    for y, x, texts, sp_info, logo in groups:
        print(f"  y={y}, x={x}")
        print(f"    Current text: {texts}")
        print(f"    Text shapes:  {sp_info}")
        print(f"    Logo image:   {logo}")
        print()

    return groups

# Run it:
# discover_all_groups('/path/to/FutureX_deck.pptx', slide_num=21, output_dir='/tmp/logos')
# Then use Read tool on each /tmp/logos/*.png to identify the companies
```

After running, use `Read` on each logo file to visually identify the company,
then build your `changes = [(shape_id, new_label), ...]` list accordingly.
