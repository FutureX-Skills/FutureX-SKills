const WEBHOOK_URL = process.env.FEISHU_FEEDBACK_WEBHOOK;

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { skillName, author, feedback } = req.body || {};
  if (typeof skillName !== 'string' || typeof feedback !== 'string' || !skillName.trim() || !feedback.trim()) {
    return res.status(400).json({ error: 'Missing skillName or feedback' });
  }
  if (!WEBHOOK_URL) {
    return res.status(503).json({ error: 'Feedback service is not configured' });
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

    if (!response.ok || data.code !== 0) {
      console.error('Webhook error:', data);
      return res.status(500).json({ error: data });
    }

    return res.status(200).json({ success: true });
  } catch (e) {
    console.error('Error:', e);
    return res.status(500).json({ error: e.message });
  }
}
