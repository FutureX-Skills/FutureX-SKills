export default async function handler(req, res) {
  if (req.method !== 'GET') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  return res.status(501).json({
    error: 'Feedback listing is not configured. Feedback is delivered to the Feishu webhook only.'
  });
}
