const AIRTABLE_API_KEY = process.env.AIRTABLE_API_KEY;
const AIRTABLE_BASE_ID = process.env.AIRTABLE_BASE_ID;
const AIRTABLE_TABLE = 'Feedback';

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { skillName, feedback, version } = req.body;

  if (!skillName || !feedback) {
    return res.status(400).json({ error: 'Missing skillName or feedback' });
  }

  if (!AIRTABLE_API_KEY || !AIRTABLE_BASE_ID) {
    return res.status(500).json({
      error: 'Airtable not configured',
      debug: { hasKey: !!AIRTABLE_API_KEY, hasBase: !!AIRTABLE_BASE_ID }
    });
  }

  const timestamp = new Date().toISOString();

  try {
    const response = await fetch(`https://api.airtable.com/v0/${AIRTABLE_BASE_ID}/${AIRTABLE_TABLE}`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${AIRTABLE_API_KEY}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        records: [{
          fields: {
            'Skill Name': skillName,
            'Feedback': feedback.trim(),
            'Timestamp': timestamp
          }
        }]
      })
    });

    const data = await response.json();

    if (!response.ok) {
      console.error('Airtable error:', data);
      return res.status(500).json({ error: data });
    }

    return res.status(200).json({ success: true });
  } catch (e) {
    console.error('Error:', e);
    return res.status(500).json({ error: e.message });
  }
}