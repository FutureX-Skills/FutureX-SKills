export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { skillName, feedback, version } = req.body;

  if (!skillName || !feedback) {
    return res.status(400).json({ error: 'Missing skillName or feedback' });
  }

  const timestamp = new Date().toISOString();
  const entry = {
    id: Date.now().toString(36),
    skillName,
    feedback: feedback.trim(),
    version: version || 'unknown',
    timestamp
  };

  // Vercel Serverless 用 /tmp 目录
  const fs = require('fs/promises');
  const path = require('path');

  const dataDir = '/tmp';
  const filePath = path.join(dataDir, 'feedback.json');

  let existing = [];
  try {
    const data = await fs.readFile(filePath, 'utf-8');
    existing = JSON.parse(data);
  } catch (e) {
    // 文件不存在
  }

  existing.unshift(entry);

  try {
    await fs.writeFile(filePath, JSON.stringify(existing, null, 2));
  } catch (e) {
    console.error('Write error:', e);
  }

  return res.status(200).json({
    success: true,
    message: 'Feedback submitted successfully'
  });
}