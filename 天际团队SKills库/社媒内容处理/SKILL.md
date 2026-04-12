---
name: social-media-processor
description: 社交媒体图片视频处理自动化 skill，基于 ffmpeg + ImageMagick/Pillow。支持图片加水印/中日英文字标注、视频拼接合并、社交媒体平台尺寸适配（小红书/Twitter/Instagram 等）。当用户提到"加水印"、"图片标注"、"文字覆盖"、"视频合并"、"视频拼接"、"社交媒体尺寸"、"小红书"、"Twitter图片"、"Instagram适配"、或任何涉及图片文字处理和视频拼接的需求时，都应触发此 skill。即使用户只是简单说"帮我处理一下图片"或"把几个视频拼在一起"，也应该使用此 skill。
---

# 社交媒体图片视频处理 Skill

一站式处理图片和视频，输出适合社交媒体发布的内容。

---

## 前置依赖

```bash
# 安装 ffmpeg（视频处理核心）
apt-get update && apt-get install -y ffmpeg imagemagick

# 安装 Python 图片处理库
pip install Pillow --break-system-packages
```

运行任何操作前，先确认依赖已安装：
```bash
ffmpeg -version && convert -version && python3 -c "from PIL import Image; print('Pillow OK')"
```

---

## 一、社交媒体平台尺寸预设

不同平台对图片/视频有不同的最佳尺寸，处理前先确认目标平台：

| 平台 | 图片尺寸（推荐） | 视频尺寸 | 视频时长限制 |
|------|-----------------|---------|-------------|
| 小红书 | 1080×1440 (3:4) | 1080×1440 | 15分钟 |
| Twitter/X | 1200×675 (16:9) | 1920×1080 | 2分20秒 |
| Instagram Feed | 1080×1080 (1:1) | 1080×1080 | 60秒 |
| Instagram Story | 1080×1920 (9:16) | 1080×1920 | 60秒 |
| 抖音/TikTok | 1080×1920 (9:16) | 1080×1920 | 10分钟 |
| YouTube Shorts | 1080×1920 (9:16) | 1080×1920 | 60秒 |

当用户指定平台时，自动选择对应预设；未指定则默认询问或使用 1080×1080。

---

## 二、图片加水印 / 文字标注

使用 Python Pillow 进行图片文字处理。选择 Pillow 而非 ImageMagick 的原因是：Pillow 对 CJK（中日韩）字体支持更可控。

### 核心 Python 脚本

```python
from PIL import Image, ImageDraw, ImageFont
import os

def add_text_to_image(
    input_path,
    output_path,
    text,
    position="bottom_center",    # top_left / top_center / top_right / center / bottom_left / bottom_center / bottom_right
    font_size=48,
    font_color=(255, 255, 255),  # RGB 白色
    bg_color=(0, 0, 0, 160),    # RGBA 半透明黑底
    padding=20,
    font_path=None,
    target_size=None             # 目标尺寸 (width, height)，用于社交媒体适配
):
    img = Image.open(input_path).convert("RGBA")

    # 如果指定了目标尺寸，先 resize + 居中裁剪
    if target_size:
        img = resize_and_crop(img, target_size)

    # 选择字体 — 优先使用系统中日韩字体
    font = get_cjk_font(font_size, font_path)

    # 创建文字层
    txt_layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(txt_layer)

    # 计算文字尺寸和位置
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]

    x, y = calculate_position(position, img.size, text_w, text_h, padding)

    # 画半透明背景
    if bg_color:
        draw.rectangle(
            [x - padding, y - padding//2, x + text_w + padding, y + text_h + padding//2],
            fill=bg_color
        )

    # 写文字
    draw.text((x, y), text, font=font, fill=font_color)

    # 合并并保存
    result = Image.alpha_composite(img, txt_layer).convert("RGB")
    result.save(output_path, quality=95)
    print(f"✅ 已保存: {output_path}")


def add_watermark(
    input_path,
    output_path,
    watermark_text,
    opacity=80,                  # 水印透明度 0-255
    font_size=36,
    position="bottom_right",
    font_path=None
):
    """专门用于加水印，比文字标注更轻量、更透明"""
    img = Image.open(input_path).convert("RGBA")
    font = get_cjk_font(font_size, font_path)

    txt_layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(txt_layer)

    bbox = draw.textbbox((0, 0), watermark_text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]

    x, y = calculate_position(position, img.size, text_w, text_h, padding=30)

    # 水印颜色半透明白
    draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, opacity))

    result = Image.alpha_composite(img, txt_layer).convert("RGB")
    result.save(output_path, quality=95)
    print(f"✅ 水印已添加: {output_path}")


def resize_and_crop(img, target_size):
    """智能缩放+居中裁剪，适配社交媒体尺寸"""
    target_w, target_h = target_size
    img_w, img_h = img.size
    target_ratio = target_w / target_h
    img_ratio = img_w / img_h

    if img_ratio > target_ratio:
        # 图片更宽，按高度缩放后裁宽
        new_h = target_h
        new_w = int(img_ratio * new_h)
    else:
        # 图片更高，按宽度缩放后裁高
        new_w = target_w
        new_h = int(new_w / img_ratio)

    img = img.resize((new_w, new_h), Image.LANCZOS)
    left = (new_w - target_w) // 2
    top = (new_h - target_h) // 2
    return img.crop((left, top, left + target_w, top + target_h))


def get_cjk_font(size, custom_path=None):
    """按优先级查找支持中日韩的字体"""
    if custom_path and os.path.exists(custom_path):
        return ImageFont.truetype(custom_path, size)

    # 常见 CJK 字体路径（按系统环境排列）
    candidates = [
        "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/noto-cjk/NotoSansCJK-Regular.ttc",
        "/System/Library/Fonts/PingFang.ttc",                      # macOS
        "/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc",           # macOS 日语
        "C:/Windows/Fonts/msyh.ttc",                               # Windows 微软雅黑
        "C:/Windows/Fonts/YuGothR.ttc",                            # Windows 日语
    ]
    for path in candidates:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)

    # 兜底：尝试安装 Noto 字体
    os.system("apt-get install -y fonts-noto-cjk 2>/dev/null")
    for path in candidates[:3]:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)

    print("⚠️ 未找到 CJK 字体，中日文可能显示为方块")
    return ImageFont.load_default()


def calculate_position(position, img_size, text_w, text_h, padding):
    """根据位置关键词计算坐标"""
    w, h = img_size
    positions = {
        "top_left":      (padding, padding),
        "top_center":    ((w - text_w) // 2, padding),
        "top_right":     (w - text_w - padding, padding),
        "center":        ((w - text_w) // 2, (h - text_h) // 2),
        "bottom_left":   (padding, h - text_h - padding),
        "bottom_center": ((w - text_w) // 2, h - text_h - padding),
        "bottom_right":  (w - text_w - padding, h - text_h - padding),
    }
    return positions.get(position, positions["bottom_center"])


# 批量处理函数
def batch_process(input_dir, output_dir, text, **kwargs):
    """批量给目录下所有图片加文字"""
    os.makedirs(output_dir, exist_ok=True)
    extensions = {'.jpg', '.jpeg', '.png', '.webp', '.bmp'}
    for f in sorted(os.listdir(input_dir)):
        if os.path.splitext(f)[1].lower() in extensions:
            add_text_to_image(
                os.path.join(input_dir, f),
                os.path.join(output_dir, f),
                text,
                **kwargs
            )
```

### 常用调用示例

```python
# 1. 给图片加中文水印
add_watermark("photo.jpg", "photo_wm.jpg", "© 我的账号")

# 2. 日语标注 + 小红书尺寸适配
add_text_to_image(
    "photo.jpg", "photo_xhs.jpg",
    "東京タワーからの眺め 🗼",
    target_size=(1080, 1440),  # 小红书 3:4
    position="bottom_center",
    font_size=56
)

# 3. 英文标注 + Twitter 尺寸
add_text_to_image(
    "photo.jpg", "photo_tw.jpg",
    "Osaka Castle at sunset",
    target_size=(1200, 675),   # Twitter 16:9
    position="bottom_left",
    font_size=40
)

# 4. 批量加水印
batch_process("./photos/", "./output/", "© MyBrand", position="bottom_right", font_size=32)
```

---

## 三、视频拼接 / 合并

使用 ffmpeg concat 功能，支持相同编码直接拼接（快速）和不同编码重新编码拼接（兼容性好）。

### 方式 A：相同编码快速拼接（推荐，速度极快）

当所有视频的分辨率、编码、帧率一致时使用：

```bash
# 1. 创建文件列表
cat > filelist.txt << 'EOF'
file '/path/to/video1.mp4'
file '/path/to/video2.mp4'
file '/path/to/video3.mp4'
EOF

# 2. 拼接
ffmpeg -f concat -safe 0 -i filelist.txt -c copy output.mp4
```

### 方式 B：不同编码/尺寸的视频合并（通用但较慢）

当视频参数不一致时，需要重新编码统一规格：

```bash
# 先将每个视频统一为相同规格
for f in video1.mp4 video2.mp4 video3.mp4; do
    ffmpeg -i "$f" \
        -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black" \
        -r 30 \
        -c:v libx264 -preset fast -crf 23 \
        -c:a aac -ar 44100 -ac 2 \
        "normalized_${f}"
done

# 然后拼接
cat > filelist.txt << 'EOF'
file 'normalized_video1.mp4'
file 'normalized_video2.mp4'
file 'normalized_video3.mp4'
EOF

ffmpeg -f concat -safe 0 -i filelist.txt -c copy final_output.mp4
```

### 方式 C：Python 脚本自动判断并拼接

```python
import subprocess
import json
import os

def get_video_info(path):
    """获取视频的编码/尺寸/帧率信息"""
    cmd = [
        "ffprobe", "-v", "quiet", "-print_format", "json",
        "-show_streams", "-show_format", path
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return json.loads(result.stdout)

def concat_videos(video_paths, output_path, target_size=None, platform=None):
    """
    智能拼接视频
    - video_paths: 视频文件路径列表
    - output_path: 输出路径
    - target_size: 目标尺寸 (width, height)，不指定则使用第一个视频的尺寸
    - platform: 平台名（xiaohongshu / twitter / instagram / tiktok）
    """
    # 平台预设
    platform_sizes = {
        "xiaohongshu": (1080, 1440),
        "xhs": (1080, 1440),
        "小红书": (1080, 1440),
        "twitter": (1920, 1080),
        "x": (1920, 1080),
        "instagram": (1080, 1080),
        "instagram_story": (1080, 1920),
        "tiktok": (1080, 1920),
        "抖音": (1080, 1920),
        "youtube_shorts": (1080, 1920),
    }

    if platform and not target_size:
        target_size = platform_sizes.get(platform.lower())

    # 检查所有视频是否参数一致
    infos = [get_video_info(p) for p in video_paths]
    need_reencode = not all_same_params(infos) or target_size is not None

    if need_reencode:
        w, h = target_size or get_first_resolution(infos)
        normalized = []
        for i, vpath in enumerate(video_paths):
            norm_path = f"/tmp/norm_{i}.mp4"
            subprocess.run([
                "ffmpeg", "-y", "-i", vpath,
                "-vf", f"scale={w}:{h}:force_original_aspect_ratio=decrease,pad={w}:{h}:(ow-iw)/2:(oh-ih)/2:black",
                "-r", "30",
                "-c:v", "libx264", "-preset", "fast", "-crf", "23",
                "-c:a", "aac", "-ar", "44100", "-ac", "2",
                norm_path
            ], check=True)
            normalized.append(norm_path)

        # 写入文件列表并拼接
        list_path = "/tmp/concat_list.txt"
        with open(list_path, "w") as f:
            for p in normalized:
                f.write(f"file '{p}'\n")
        subprocess.run([
            "ffmpeg", "-y", "-f", "concat", "-safe", "0",
            "-i", list_path, "-c", "copy", output_path
        ], check=True)

        # 清理临时文件
        for p in normalized:
            os.remove(p)
    else:
        list_path = "/tmp/concat_list.txt"
        with open(list_path, "w") as f:
            for p in video_paths:
                f.write(f"file '{os.path.abspath(p)}'\n")
        subprocess.run([
            "ffmpeg", "-y", "-f", "concat", "-safe", "0",
            "-i", list_path, "-c", "copy", output_path
        ], check=True)

    print(f"✅ 视频拼接完成: {output_path}")


def all_same_params(infos):
    """检查所有视频参数是否一致"""
    first = get_video_stream(infos[0])
    for info in infos[1:]:
        vs = get_video_stream(info)
        if (vs.get("width") != first.get("width") or
            vs.get("height") != first.get("height") or
            vs.get("codec_name") != first.get("codec_name")):
            return False
    return True


def get_video_stream(info):
    for s in info.get("streams", []):
        if s.get("codec_type") == "video":
            return s
    return {}


def get_first_resolution(infos):
    vs = get_video_stream(infos[0])
    return (vs.get("width", 1080), vs.get("height", 1920))
```

### 常用调用示例

```python
# 1. 拼接视频，适配小红书
concat_videos(
    ["clip1.mp4", "clip2.mp4", "clip3.mp4"],
    "xiaohongshu_final.mp4",
    platform="小红书"
)

# 2. 拼接视频，适配 Twitter
concat_videos(
    ["intro.mp4", "main.mp4", "outro.mp4"],
    "twitter_post.mp4",
    platform="twitter"
)

# 3. 自定义尺寸拼接
concat_videos(
    ["a.mp4", "b.mp4"],
    "custom.mp4",
    target_size=(1920, 1080)
)
```

---

## 四、完整工作流示例

用户说："帮我把这 3 张照片加上日语标注，调整成小红书尺寸，然后把 2 个视频拼接起来也发小红书"

### 步骤

1. **安装依赖**
```bash
apt-get update && apt-get install -y ffmpeg fonts-noto-cjk
pip install Pillow --break-system-packages
```

2. **处理图片**（使用上面的 Python 函数）
```python
texts = ["東京の朝 🌅", "大阪城 🏯", "京都の竹林 🎋"]
for i, (img, text) in enumerate(zip(["img1.jpg", "img2.jpg", "img3.jpg"], texts)):
    add_text_to_image(img, f"xhs_{i+1}.jpg", text, target_size=(1080, 1440))
```

3. **拼接视频**
```python
concat_videos(["video1.mp4", "video2.mp4"], "xhs_video.mp4", platform="小红書")
```

4. **输出**到 `/mnt/user-data/outputs/`

---

## 故障排查

### 中日文字显示为方块
字体缺失。安装 Noto CJK 字体：
```bash
apt-get install -y fonts-noto-cjk
```

### 视频拼接后音画不同步
不同编码的视频直接 `-c copy` 可能导致问题，改用方式 B（重新编码）。

### 图片输出模糊
检查 `quality` 参数（JPEG 推荐 95）和 `target_size` 是否远大于原图分辨率（不要放大）。

### ffmpeg 报错 "unsafe file name"
在 concat 命令中加 `-safe 0` 参数。
