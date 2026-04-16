import { readFile } from 'fs/promises';
import { join } from 'path';

export default async function handler(req, res) {
  if (req.method !== 'GET') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  // 简单保护：URL 带 ?key=fxskill 才可以看
  if (req.query.key !== 'fxskill') {
    return res.status(403).json({ error: 'Forbidden' });
  }

  const filePath = join('/tmp', 'feedback.json');

  try {
    const data = await readFile(filePath, 'utf-8');
    const feedback = JSON.parse(data);
    return res.status(200).json({ feedback });
  } catch (e) {
    return res.status(200).json({ feedback: [] });
  }
}