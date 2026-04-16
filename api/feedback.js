export default async function handler(request, response) {
  if (request.method !== 'POST') {
    return response.status(405).json({ error: 'Method not allowed' });
  }

  const { skillName, feedback, version } = request.body;

  if (!skillName || !feedback) {
    return response.status(400).json({ error: 'Missing skillName or feedback' });
  }

  const timestamp = new Date().toISOString();
  const entry = {
    id: Date.now().toString(36),
    skillName,
    feedback: feedback.trim(),
    version: version || 'unknown',
    timestamp,
    userAgent: request.headers.get('user-agent') || 'unknown'
  };

  // 存储到 JSON 文件（Vercel Serverless 文件系统）
  const fs = await import('fs/promises');
  const path = await import('path');

  const dataDir = path.join(process.cwd(), 'data');
  const filePath = path.join(dataDir, 'feedback.json');

  let existing = [];
  try {
    const data = await fs.readFile(filePath, 'utf-8');
    existing = JSON.parse(data);
  } catch (e) {
    // 文件不存在，从头开始
  }

  existing.unshift(entry); // 新反馈放前面

  try {
    await fs.mkdir(dataDir, { recursive: true });
    await fs.writeFile(filePath, JSON.stringify(existing, null, 2));
  } catch (e) {
    console.error('Write error:', e);
  }

  return response.status(200).json({
    success: true,
    message: 'Feedback submitted successfully',
    entryId: entry.id
  });
}