# 公众号文章排版

把文字内容转成公众号可用的HTML格式，参考天际一贯风格。

## 风格特点（必学）

### 标题
- 大标题：居中，18-20px，加粗
- 副标题：居中，灰色，14-15px
- 作者：右上角小灰字

### 标题（蓝色框线风格）
```html
<div style="border: 2px solid #2196F3; border-radius: 8px; padding: 15px; margin: 10px 0; text-align: center;">
  <h1 style="margin: 0; font-size: 20px; color: #333;">标题文字</h1>
</div>
```

### 正文
- 行间距：1.8-2em
- 段落间距：1em
- 首行缩进：2em（可选）
- 字体：16-17px

### 章节标题
- 带emoji：📌 🔍 💡 ⚠️ ✅ 🎯
- 粗体
- 不缩进

### 重点提示
```html
<!-- 黄色警告 -->
<div style="background: #FFF9E6; border-left: 4px solid #FFC107; padding: 12px; margin: 10px 0; border-radius: 4px;">
  ⚠️ 重点内容
</div>

<!-- 绿色成功 -->
<div style="background: #E8F5E9; border-left: 4px solid #4CAF50; padding: 12px; margin: 10px 0; border-radius: 4px;">
  ✅ 成功提示
</div>

<!-- 蓝色信息 -->
<div style="background: #E3F2FD; border-left: 4px solid #2196F3; padding: 12px; margin: 10px 0; border-radius: 4px;">
  💡 信息提示
</div>
```

### 引用
```html
<blockquote style="border-left: 3px solid #999; padding-left: 15px; margin: 15px 0; color: #666; font-style: italic;">
  引用内容
</blockquote>
```

### 表格
```html
<table border="1" cellpadding="10" cellspacing="0" style="border-collapse: collapse; width: 100%; margin: 10px 0;">
  <thead style="background: #f5f5f5;">
    <tr><th>标题</th><th>内容</th></tr>
  </thead>
  <tbody>
    <tr><td>行1</td><td>内容</td></tr>
    <tr style="background: #fafafa;"><td>行2</td><td>内容</td></tr>
  </tbody>
</table>
```

### 分割线
```html
<hr style="border: none; border-top: 1px solid #eee; margin: 20px 0;" />
```

### 结尾（天际统一版）
```html
<div style="text-align: center; margin: 30px 0;">
  <p style="font-size: 16px; color: #666;">— ✦ 往期回顾 ✦ —</p>
  <p style="font-size: 16px; margin-top: 15px;">从亚布力到禾木：一个VC的"读山"笔记——在AI长坡中寻找雪球式回报 <a href="#" style="color: #2196F3;">🔼</a></p>
  <p style="font-size: 16px; margin-top: 8px;">天际资本独家投资灵核数智Pre-A轮融资，共筑AI制造新生态｜天际portfolio <a href="#" style="color: #2196F3;">🔼</a></p>
</div>

<hr style="border: none; border-top: 1px solid #eee; margin: 20px 0;" />

<div style="font-size: 12px; line-height: 1.8; color: #999;">
  <p style="margin-bottom: 8px;"><strong>天际科技投资（FutureX Capital）</strong>由前华夏基金私募股权创始团队于2018年初主导创立。公司专注于投资中国成长期高新科技企业，重点聚焦颠覆式创新的卓越企业，重视价值创造，聚焦产业赋能，深度参与到企业发展的全周期。</p>
  <p style="margin-bottom: 8px;">全球创新技术含金量最高的公司和快速爆发下游应用是天际科技投资最关注的目标企业，并善于将这些先进技术公司推向产业平台，协助其进一步发挥潜力。代表性投资包括：金山云，字节跳动，美团，蔚来汽车，PingCAP，统信，思特威，芯盟科技，开源中国等。</p>
  <p>天际科技投资秉承开源理念，不断吸引广泛的产业资源、金融资源和专家网络，与顶级企业家进行多方位的交流与合作，汇聚顶级认知，形成前瞻性洞见和跨行业合力，通过不断提升认知，持续发掘改善世界的投资机会。</p>
</div>
```

## 使用方法

1. 用户提供文章内容
2. 选择风格（简约/卡片/原有风格）
3. 生成排版好的HTML

## 输出

- 直接可复制到公众号后台
- 样式内联，无需外部CSS
