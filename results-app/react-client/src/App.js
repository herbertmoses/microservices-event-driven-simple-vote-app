import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [summary, setSummary] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('http://localhost:8001/summary')
      .then(res => res.json())
      .then(data => {
        setSummary(data);
        setLoading(false);
      })
      .catch(err => {
        console.error("Failed to fetch summary:", err);
        setLoading(false);
      });
  }, []);

  return (
    <div className="App">
      <h1>🗳️ Voting Results</h1>
      {loading ? (
        <p>Loading results...</p>
      ) : summary ? (
        <div>
          <p><strong>Blue:</strong> {summary.blue || 0}</p>
          <p><strong>Green:</strong> {summary.green || 0}</p>
        </div>
      ) : (
        <p>Failed to load voting summary.</p>
      )}
    </div>
  );
}

export default App;
