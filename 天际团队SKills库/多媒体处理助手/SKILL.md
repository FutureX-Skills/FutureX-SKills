# media-processor Skill 文档

## 简介

多媒体文件处理工具，支持图片处理（调整大小、裁剪、滤镜、格式转换）和 PDF 处理（文字编辑、图片插入、页面操作、合并拆分、压缩）。

---

## 目录结构

```
media-processor/
├── SKILL.md
└── scripts/
    ├── image_processor.py    # 图片处理脚本
    └── pdf_processor.py      # PDF 处理脚本
```

---

## 依赖安装

```bash
# 图片处理依赖
pip install Pillow

# PDF 处理依赖
pip install pikepdf PyMuPDF
```

---

## 图片处理 (image_processor.py)

### 功能概述

| 功能 | 命令 |
|------|------|
| 调整大小 | resize |
| 裁剪 | crop |
| 滤镜效果 | filter |
| 格式转换 | convert |
| 获取信息 | info |

### 调整大小

```bash
# 按宽度等比例缩放
python3 image_processor.py resize input.jpg output.jpg --width 800

# 按高度等比例缩放
python3 image_processor.py resize input.jpg output.jpg --height 600

# 按缩放比例 (0.5 = 50%)
python3 image_processor.py resize input.jpg output.jpg --scale 0.5

# 指定宽高（可能变形）
python3 image_processor.py resize input.jpg output.jpg --width 800 --height 600 --no-keep-aspect
```

### 裁剪

```bash
python3 image_processor.py crop input.jpg output.jpg --left 100 --top 100 --right 500 --bottom 400
```

参数说明：
- `--left`: 左边界像素
- `--top`: 上边界像素
- `--right`: 右边界像素
- `--bottom`: 下边界像素

### 滤镜效果

```bash
python3 image_processor.py filter input.jpg output.jpg --type <滤镜类型>
```

可用滤镜类型：

| 滤镜 | 说明 |
|------|------|
| blur | 模糊 |
| sharpen | 锐化 |
| contour | 轮廓 |
| emboss | 浮雕 |
| edge_enhance | 边缘增强 |
| smooth | 平滑 |
| grayscale | 灰度 |
| sepia | 复古/ sepia 色调 |
| brightness | 亮度增加 |
| contrast | 对比度增加 |

示例：
```bash
python3 image_processor.py filter photo.jpg bw.jpg --type grayscale
python3 image_processor.py filter photo.jpg blur.jpg --type blur
python3 image_processor.py filter photo.jpg vintage.jpg --type sepia
```

### 格式转换

```bash
python3 image_processor.py convert input.png output.jpg
python3 image_processor.py convert input.jpg output.webp
python3 image_processor.py convert input.bmp output.png
```

支持的格式：JPEG, PNG, WebP, BMP, GIF, TIFF 等

### 获取图片信息

```bash
python3 image_processor.py info input.jpg
```

输出示例：
```
format: JPEG
mode: RGB
width: 1920
height: 1080
size: 245760
```

---

## PDF 处理 (pdf_processor.py)

### 功能概述

| 功能 | 命令 |
|------|------|
| 合并 PDF | merge |
| 拆分 PDF | split |
| 旋转页面 | rotate |
| 提取文本 | extract-text |
| 替换文本 | replace-text |
| 插入图片 | insert-image |
| 获取信息 | info |
| 压缩 PDF | compress |

### 合并 PDF

```bash
python3 pdf_processor.py merge output.pdf input1.pdf input2.pdf input3.pdf
```

### 拆分 PDF

```bash
# 每 1 页拆成一个文件
python3 pdf_processor.py split input.pdf --output-dir ./pages --pages-per-file 1

# 每 5 页拆成一个文件
python3 pdf_processor.py split input.pdf --output-dir ./parts --pages-per-file 5
```

### 旋转页面

```bash
# 旋转所有页面 90 度
python3 pdf_processor.py rotate input.pdf output.pdf --angle 90

# 旋转指定页面（第1、3、5页，索引从0开始）
python3 pdf_processor.py rotate input.pdf output.pdf --angle 180 --pages 0 2 4

# 可选角度：90, 180, 270
```

### 提取文本

```bash
# 提取所有文本
python3 pdf_processor.py extract-text input.pdf

# 提取指定页面文本（第1页，索引从0开始）
python3 pdf_processor.py extract-text input.pdf --page 0
```

### 替换文本

```bash
python3 pdf_processor.py replace-text input.pdf output.pdf --old "旧文本" --new "新文本"
```

**注意**：此功能使用覆盖+重写方式，适合简单文本替换。复杂排版可能需要专业 PDF 编辑软件。

### 插入图片

```bash
python3 pdf_processor.py insert-image input.pdf output.pdf \
    --image logo.png \
    --page 0 \
    --x 100 \
    --y 100 \
    --width 200
```

参数说明：
- `--image`: 要插入的图片路径
- `--page`: 页码（从0开始）
- `--x`: X 坐标（从左边缘算起）
- `--y`: Y 坐标（从下边缘算起）
- `--width`: 图片宽度（可选，保持比例）
- `--height`: 图片高度（可选，保持比例）

**坐标系统**：PDF 坐标原点在左下角，X 向右，Y 向上。

### 获取 PDF 信息

```bash
python3 pdf_processor.py info input.pdf
```

输出示例：
```
pages: 10
version: 1.4
encrypted: False
title: 文档标题
author: 作者名
```

### 压缩 PDF

```bash
python3 pdf_processor.py compress input.pdf output.pdf --quality 80
```

参数说明：
- `--quality`: 图片质量（1-100，默认80），数值越小压缩率越高

---

## 工作流程示例

### 批量调整图片大小

```bash
# 批量将当前目录所有 jpg 图片调整为宽度 800px
for img in *.jpg; do
    python3 image_processor.py resize "$img" "resized_$img" --width 800
done
```

### 为 PDF 添加水印

```bash
# 在 PDF 第一页右上角添加水印图片
python3 pdf_processor.py insert-image document.pdf watermarked.pdf \
    --image watermark.png \
    --page 0 \
    --x 400 \
    --y 700 \
    --width 150
```

### 合并多个扫描件

```bash
python3 pdf_processor.py merge scanned_document.pdf page1.pdf page2.pdf page3.pdf
```

### 压缩 PDF 文件大小

```bash
# 高质量压缩（适合打印）
python3 pdf_processor.py compress large.pdf compressed.pdf --quality 90

# 低质量压缩（适合邮件发送）
python3 pdf_processor.py compress large.pdf compressed.pdf --quality 50
```

### 提取 PDF 所有文本到文件

```bash
python3 pdf_processor.py extract-text document.pdf > document.txt
```

### 批量转换图片格式

```bash
# 将所有 PNG 转为 JPG
for img in *.png; do
    python3 image_processor.py convert "$img" "${img%.png}.jpg"
done
```

---

## 注意事项

1. **PDF 文字编辑限制**
   - PDF 文字替换使用覆盖+重写方式
   - 适合简单文本替换（如模板填充）
   - 复杂排版、多字体混排可能需要专业 PDF 编辑软件

2. **坐标系统**
   - PDF 坐标原点在左下角
   - X 轴向右为正方向
   - Y 轴向上为正方向
   - 单位：点（1/72 英寸）

3. **依赖问题**
   - 图片处理仅需 Pillow
   - PDF 处理需要 pikepdf 和 PyMuPDF
   - 如遇中文显示问题，可能需要安装中文字体

4. **文件备份**
   - 建议在处理重要文件前先备份原文件
   - 脚本会直接覆盖输出文件

5. **性能考虑**
   - 大文件处理可能需要较长时间
   - PDF 压缩会重新编码图片，可能损失质量
   - 批量处理建议使用循环脚本

---

## 故障排除

### 安装依赖失败

```bash
# 更新 pip
pip install --upgrade pip

# 安装编译依赖（Linux）
sudo apt-get install python3-dev build-essential

# 重新安装
pip install Pillow pikepdf PyMuPDF
```

### 中文显示问题

PDF 文本提取或替换时中文显示异常，可能需要：
```bash
# 安装中文字体（Ubuntu/Debian）
sudo apt-get install fonts-wqy-zenhei fonts-wqy-microhei
```

### 权限问题

```bash
# 添加执行权限
chmod +x image_processor.py pdf_processor.py

# 或直接通过 python3 运行
python3 image_processor.py ...
```

---

## 完整脚本代码

### image_processor.py

```python
#!/usr/bin/env python3
"""
图片处理脚本 - 支持调整大小、裁剪、滤镜、格式转换
依赖: Pillow (pip install Pillow)
"""

import sys
import os
from PIL import Image, ImageFilter, ImageEnhance
import argparse


def resize_image(input_path, output_path, width=None, height=None, scale=None, keep_aspect=True):
    """调整图片大小"""
    with Image.open(input_path) as img:
        original_width, original_height = img.size
        
        if scale:
            new_width = int(original_width * scale)
            new_height = int(original_height * scale)
        elif width and height and not keep_aspect:
            new_width, new_height = width, height
        elif width:
            ratio = width / original_width
            new_width = width
            new_height = int(original_height * ratio)
        elif height:
            ratio = height / original_height
            new_height = height
            new_width = int(original_width * ratio)
        else:
            raise ValueError("必须指定 width、height 或 scale 之一")
        
        resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        resized.save(output_path)
        print(f"已调整大小: {original_width}x{original_height} -> {new_width}x{new_height}")
        return output_path


def crop_image(input_path, output_path, left, top, right, bottom):
    """裁剪图片"""
    with Image.open(input_path) as img:
        cropped = img.crop((left, top, right, bottom))
        cropped.save(output_path)
        print(f"已裁剪: ({left}, {top}) 到 ({right}, {bottom})")
        return output_path


def apply_filter(input_path, output_path, filter_type):
    """应用滤镜"""
    with Image.open(input_path) as img:
        if filter_type == "blur":
            result = img.filter(ImageFilter.GaussianBlur(radius=2))
        elif filter_type == "sharpen":
            result = img.filter(ImageFilter.SHARPEN)
        elif filter_type == "contour":
            result = img.filter(ImageFilter.CONTOUR)
        elif filter_type == "emboss":
            result = img.filter(ImageFilter.EMBOSS)
        elif filter_type == "edge_enhance":
            result = img.filter(ImageFilter.EDGE_ENHANCE)
        elif filter_type == "smooth":
            result = img.filter(ImageFilter.SMOOTH)
        elif filter_type == "grayscale":
            result = img.convert("L").convert("RGB")
        elif filter_type == "sepia":
            result = img.convert("RGB")
            pixels = result.load()
            for i in range(result.width):
                for j in range(result.height):
                    r, g, b = pixels[i, j]
                    tr = int(0.393 * r + 0.769 * g + 0.189 * b)
                    tg = int(0.349 * r + 0.686 * g + 0.168 * b)
                    tb = int(0.272 * r + 0.534 * g + 0.131 * b)
                    pixels[i, j] = (min(tr, 255), min(tg, 255), min(tb, 255))
        elif filter_type == "brightness":
            enhancer = ImageEnhance.Brightness(img)
            result = enhancer.enhance(1.2)
        elif filter_type == "contrast":
            enhancer = ImageEnhance.Contrast(img)
            result = enhancer.enhance(1.2)
        else:
            raise ValueError(f"不支持的滤镜类型: {filter_type}")
        
        result.save(output_path)
        print(f"已应用滤镜: {filter_type}")
        return output_path


def convert_format(input_path, output_path):
    """转换图片格式"""
    with Image.open(input_path) as img:
        # 处理透明通道转换
        if output_path.lower().endswith('.jpg') or output_path.lower().endswith('.jpeg'):
            if img.mode in ('RGBA', 'LA', 'P'):
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
                img = background
        img.save(output_path)
        print(f"已转换格式: {input_path} -> {output_path}")
        return output_path


def get_image_info(input_path):
    """获取图片信息"""
    with Image.open(input_path) as img:
        info = {
            "format": img.format,
            "mode": img.mode,
            "width": img.width,
            "height": img.height,
            "size": os.path.getsize(input_path)
        }
        return info


def main():
    parser = argparse.ArgumentParser(description='图片处理工具')
    subparsers = parser.add_subparsers(dest='command', help='可用命令')
    
    # resize 命令
    resize_parser = subparsers.add_parser('resize', help='调整大小')
    resize_parser.add_argument('input', help='输入文件路径')
    resize_parser.add_argument('output', help='输出文件路径')
    resize_parser.add_argument('--width', type=int, help='目标宽度')
    resize_parser.add_argument('--height', type=int, help='目标高度')
    resize_parser.add_argument('--scale', type=float, help='缩放比例')
    resize_parser.add_argument('--no-keep-aspect', action='store_true', help='不保持宽高比')
    
    # crop 命令
    crop_parser = subparsers.add_parser('crop', help='裁剪')
    crop_parser.add_argument('input', help='输入文件路径')
    crop_parser.add_argument('output', help='输出文件路径')
    crop_parser.add_argument('--left', type=int, required=True, help='左边界')
    crop_parser.add_argument('--top', type=int, required=True, help='上边界')
    crop_parser.add_argument('--right', type=int, required=True, help='右边界')
    crop_parser.add_argument('--bottom', type=int, required=True, help='下边界')
    
    # filter 命令
    filter_parser = subparsers.add_parser('filter', help='应用滤镜')
    filter_parser.add_argument('input', help='输入文件路径')
    filter_parser.add_argument('output', help='输出文件路径')
    filter_parser.add_argument('--type', required=True, 
                               choices=['blur', 'sharpen', 'contour', 'emboss', 
                                       'edge_enhance', 'smooth', 'grayscale', 
                                       'sepia', 'brightness', 'contrast'],
                               help='滤镜类型')
    
    # convert 命令
    convert_parser = subparsers.add_parser('convert', help='格式转换')
    convert_parser.add_argument('input', help='输入文件路径')
    convert_parser.add_argument('output', help='输出文件路径')
    
    # info 命令
    info_parser = subparsers.add_parser('info', help='获取图片信息')
    info_parser.add_argument('input', help='输入文件路径')
    
    args = parser.parse_args()
    
    if args.command == 'resize':
        resize_image(args.input, args.output, args.width, args.height, 
                    args.scale, not args.no_keep_aspect)
    elif args.command == 'crop':
        crop_image(args.input, args.output, args.left, args.top, args.right, args.bottom)
    elif args.command == 'filter':
        apply_filter(args.input, args.output, args.type)
    elif args.command == 'convert':
        convert_format(args.input, args.output)
    elif args.command == 'info':
        info = get_image_info(args.input)
        for key, value in info.items():
            print(f"{key}: {value}")
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
```

### pdf_processor.py

```python
#!/usr/bin/env python3
"""
PDF 处理脚本 - 支持文字编辑、图片插入、页面操作
依赖: pikepdf, Pillow, reportlab (pip install pikepdf Pillow reportlab)
"""

import sys
import os
import io
from pathlib import Path
import argparse

try:
    import pikepdf
    from pikepdf import Pdf, Page, Rectangle
except ImportError:
    print("错误: 需要安装 pikepdf (pip install pikepdf)")
    sys.exit(1)

try:
    from PIL import Image
except ImportError:
    print("错误: 需要安装 Pillow (pip install Pillow)")
    sys.exit(1)


def merge_pdfs(output_path, *input_paths):
    """合并多个 PDF 文件"""
    pdf = Pdf.new()
    for path in input_paths:
        src = Pdf.open(path)
        pdf.pages.extend(src.pages)
    pdf.save(output_path)
    print(f"已合并 {len(input_paths)} 个 PDF 到 {output_path}")
    return output_path


def split_pdf(input_path, output_dir, pages_per_file=1):
    """拆分 PDF 文件"""
    src = Pdf.open(input_path)
    base_name = Path(input_path).stem
    output_files = []
    
    for i in range(0, len(src.pages), pages_per_file):
        pdf = Pdf.new()
        end = min(i + pages_per_file, len(src.pages))
        for j in range(i, end):
            pdf.pages.append(src.pages[j])
        output_path = os.path.join(output_dir, f"{base_name}_part{i//pages_per_file + 1}.pdf")
        pdf.save(output_path)
        output_files.append(output_path)
    
    print(f"已拆分为 {len(output_files)} 个文件")
    return output_files


def rotate_pages(input_path, output_path, rotation, pages=None):
    """旋转 PDF 页面
    rotation: 90, 180, 270
    pages: 页面索引列表 (从0开始)，None表示所有页面
    """
    pdf = Pdf.open(input_path)
    page_indices = pages if pages else range(len(pdf.pages))
    
    for i in page_indices:
        if 0 <= i < len(pdf.pages):
            pdf.pages[i].Rotate = (pdf.pages[i].Rotate or 0) + rotation
    
    pdf.save(output_path)
    print(f"已旋转页面: {page_indices if pages else '所有页面'}，角度: {rotation}")
    return output_path


def extract_text(input_path, page_num=None):
    """提取 PDF 中的文本
    注意: 这是基础实现，复杂 PDF 可能需要 pdfplumber 或 PyMuPDF
    """
    try:
        import fitz  # PyMuPDF
        doc = fitz.open(input_path)
        text = ""
        if page_num is not None:
            if 0 <= page_num < len(doc):
                text = doc[page_num].get_text()
        else:
            for page in doc:
                text += page.get_text() + "\n---\n"
        doc.close()
        return text
    except ImportError:
        print("提示: 安装 PyMuPDF (pip install PyMuPDF) 可获得更好的文本提取效果")
        return "文本提取需要 PyMuPDF 库"


def replace_text_in_pdf(input_path, output_path, replacements):
    """
    在 PDF 中替换文本
    replacements: dict, 例如 {'旧文本': '新文本'}
    注意: 这使用简单的方法，复杂 PDF 可能需要更高级的处理
    """
    try:
        import fitz  # PyMuPDF
        doc = fitz.open(input_path)
        
        for page in doc:
            for old_text, new_text in replacements.items():
                text_instances = page.search_for(old_text)
                for inst in text_instances:
                    # 用白色矩形覆盖原文本
                    page.add_redact_annot(inst, fill=(1, 1, 1))
                    page.apply_redactions()
                    # 插入新文本
                    page.insert_text(inst.tl, new_text, fontsize=11)
        
        doc.save(output_path)
        doc.close()
        print(f"已替换文本并保存到 {output_path}")
        return output_path
    except ImportError:
        print("错误: 文本编辑需要 PyMuPDF (pip install PyMuPDF)")
        return None


def insert_image_to_pdf(input_path, output_path, image_path, page_num, x, y, width=None, height=None):
    """
    在 PDF 指定位置插入图片
    """
    try:
        import fitz  # PyMuPDF
        doc = fitz.open(input_path)
        
        if page_num < 0 or page_num >= len(doc):
            print(f"错误: 页码 {page_num} 超出范围 (0-{len(doc)-1})")
            return None
        
        page = doc[page_num]
        
        # 计算图片尺寸
        with Image.open(image_path) as img:
            img_width, img_height = img.size
            if width and not height:
                height = width * img_height / img_width
            elif height and not width:
                width = height * img_width / img_height
            elif not width and not height:
                width = img_width
                height = img_height
        
        rect = fitz.Rect(x, y, x + width, y + height)
        page.insert_image(rect, filename=image_path)
        
        doc.save(output_path)
        doc.close()
        print(f"已在第 {page_num+1} 页插入图片")
        return output_path
    except ImportError:
        print("错误: 图片插入需要 PyMuPDF (pip install PyMuPDF)")
        return None


def get_pdf_info(input_path):
    """获取 PDF 信息"""
    pdf = Pdf.open(input_path)
    info = {
        "pages": len(pdf.pages),
        "version": pdf.pdf_version,
        "encrypted": pdf.is_encrypted,
    }
    if "/Info" in pdf.root:
        pdf_info = pdf.root.Info
        for key in ["/Title", "/Author", "/Subject", "/Creator", "/Producer"]:
            if key in pdf_info:
                info[key[1:].lower()] = str(pdf_info[key])
    return info


def compress_pdf(input_path, output_path, image_quality=80):
    """压缩 PDF 文件"""
    try:
        import fitz  # PyMuPDF
        doc = fitz.open(input_path)
        
        for page in doc:
            images = page.get_images()
            for img_index, img in enumerate(images):
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]
                
                # 压缩图片
                if image_ext in ['jpeg', 'jpg', 'png']:
                    from PIL import Image
                    img_pil = Image.open(io.BytesIO(image_bytes))
                    output = io.BytesIO()
                    if image_ext in ['jpeg', 'jpg']:
                        img_pil.save(output, format='JPEG', quality=image_quality, optimize=True)
                    else:
                        img_pil.save(output, format='PNG', optimize=True)
                    doc.update_stream(xref, output.getvalue())
        
        doc.save(output_path, garbage=4, deflate=True)
        doc.close()
        
        original_size = os.path.getsize(input_path)
        new_size = os.path.getsize(output_path)
        reduction = (original_size - new_size) / original_size * 100
        print(f"已压缩: {original_size/1024:.1f}KB -> {new_size/1024:.1f}KB (减少 {reduction:.1f}%)")
        return output_path
    except ImportError:
        print("错误: PDF 压缩需要 PyMuPDF (pip install PyMuPDF)")
        return None


def main():
    parser = argparse.ArgumentParser(description='PDF 处理工具')
    subparsers = parser.add_subparsers(dest='command', help='可用命令')
    
    # merge 命令
    merge_parser = subparsers.add_parser('merge', help='合并 PDF')
    merge_parser.add_argument('output', help='输出文件路径')
    merge_parser.add_argument('inputs', nargs='+', help='输入文件路径')
    
    # split 命令
    split_parser = subparsers.add_parser('split', help='拆分 PDF')
    split_parser.add_argument('input', help='输入文件路径')
    split_parser.add_argument('--output-dir', required=True, help='输出目录')
    split_parser.add_argument('--pages-per-file', type=int, default=1, help='每个文件的页数')
    
    # rotate 命令
    rotate_parser = subparsers.add_parser('rotate', help='旋转页面')
    rotate_parser.add_argument('input', help='输入文件路径')
    rotate_parser.add_argument('output', help='输出文件路径')
    rotate_parser.add_argument('--angle', type=int, required=True, choices=[90, 180, 270], help='旋转角度')
    rotate_parser.add_argument('--pages', type=int, nargs='+', help='要旋转的页面索引 (从0开始)')
    
    # info 命令
    info_parser = subparsers.add_parser('info', help='获取 PDF 信息')
    info_parser.add_argument('input', help='输入文件路径')
    
    # extract-text 命令
    text_parser = subparsers.add_parser('extract-text', help='提取文本')
    text_parser.add_argument('input', help='输入文件路径')
    text_parser.add_argument('--page', type=int, help='指定页码 (从0开始)')
    
    # replace-text 命令
    replace_parser = subparsers.add_parser('replace-text', help='替换文本')
    replace_parser.add_argument('input', help='输入文件路径')
    replace_parser.add_argument('output', help='输出文件路径')
    replace_parser.add_argument('--old', required=True, help='要替换的文本')
    replace_parser.add_argument('--new', required=True, help='新文本')
    
    # insert-image 命令
    img_parser = subparsers.add_parser('insert-image', help='插入图片')
    img_parser.add_argument('input', help='输入文件路径')
    img_parser.add_argument('output', help='输出文件路径')
    img_parser.add_argument('--image', required=True, help='要插入的图片路径')
    img_parser.add_argument('--page', type=int, required=True, help='页码 (从0开始)')
    img_parser.add_argument('--x', type=float, required=True, help='X 坐标')
    img_parser.add_argument('--y', type=float, required=True, help='Y 坐标')
    img_parser.add_argument('--width', type=float, help='宽度')
    img_parser.add_argument('--height', type=float, help='高度')
    
    # compress 命令
    compress_parser = subparsers.add_parser('compress', help='压缩 PDF')
    compress_parser.add_argument('input', help='输入文件路径')
    compress_parser.add_argument('output', help='输出文件路径')
    compress_parser.add_argument('--quality', type=int, default=80, help='图片质量 (1-100)')
    
    args = parser.parse_args()
    
    if args.command == 'merge':
        merge_pdfs(args.output, *args.inputs)
    elif args.command == 'split':
        os.makedirs(args.output_dir, exist_ok=True)
        split_pdf(args.input, args.output_dir, args.pages_per_file)
    elif args.command == 'rotate':
        rotate_pages(args.input, args.output, args.angle, args.pages)
    elif args.command == 'info':
        info = get_pdf_info(args.input)
        for key, value in info.items():
            print(f"{key}: {value}")
    elif args.command == 'extract-text':
        text = extract_text(args.input, args.page)
        print(text)
    elif args.command == 'replace-text':
        replace_text_in_pdf(args.input, args.output, {args.old: args.new})
    elif args.command == 'insert-image':
        insert_image_to_pdf(args.input, args.output, args.image, 
                           args.page, args.x, args.y, args.width, args.height)
    elif args.command == 'compress':
        compress_pdf(args.input, args.output, args.quality)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
```

---

**文档版本**: 1.0  
**创建日期**: 2026-03-16  
**作者**: OpenClaw Assistant
