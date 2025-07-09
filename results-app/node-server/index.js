import express from 'express';
import path from 'path';
import axios from 'axios';
import { fileURLToPath } from 'url';
import { dirname } from 'path';

// Resolve __dirname manually in ES modules
const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const app = express();
const PORT = 8084;

// Serve React static files
app.use(express.static(path.join(__dirname, '../client/build')));

// Proxy API to FastAPI worker-app
app.get('/api/summary', async (req, res) => {
  try {
    const response = await axios.get('http://localhost:8001/summary');
    res.json(response.data);
  } catch (error) {
    console.error('Error fetching summary:', error.message);
    res.status(500).json({ error: 'Failed to fetch vote summary' });
  }
});

// Fallback to index.html for React routes
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, '../client/build/index.html'));
});

app.listen(PORT, () => {
  console.log(`✅ Results backend running at http://localhost:${PORT}`);
});
