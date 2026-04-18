const WEBHOOK_URL = 'https://open.feishu.cn/open-apis/bot/v2/hook/ddb5e757-2a4b-486d-86a9-37a4d73a617a';

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { skillName, author, feedback } = req.body;
  if (!skillName || !feedback) {
    return res.status(400).json({ error: 'Missing skillName or feedback' });
  }

  try {
    const timestamp = new Date().toLocaleDateString('zh-CN', { timeZone: 'Asia/Shanghai' }).replace(/\//g, '-');
    const message = {
      msg_type: 'text',
      content: JSON.stringify({
        text: `👻 新反馈\n\n👾 Skill: ${skillName}\n👤 创建人: ${author || '外部精选'}\n📮 反馈: ${feedback.trim()}\n📅 时间: ${timestamp}`
      })
    };

    const response = await fetch(WEBHOOK_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(message)
    });

    const data = await response.json();

    if (!response.ok) {
      console.error('Webhook error:', data);
      return res.status(500).json({ error: data });
    }

    return res.status(200).json({ success: true });
  } catch (e) {
    console.error('Error:', e);
    return res.status(500).json({ error: e.message });
  }
}