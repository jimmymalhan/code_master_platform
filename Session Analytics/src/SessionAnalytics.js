import React, { useEffect, useState } from 'react';

function SessionAnalytics() {
  const [sessionData, setSessionData] = useState(null);

  useEffect(() => {
    // Fetch the JSON data from your Python script's API endpoint
    fetch('/api/calculated_sessions.json')
      .then((response) => response.json())
      .then((data) => {
        // Set the retrieved session data in the state
        setSessionData(data);
      })
      .catch((error) => {
        console.error('Error fetching session data:', error);
      });
  }, []);

  return (
    <div>
      <h1>Session Analytics</h1>
      {sessionData && (
        <div>
          <h2>Sessions by User</h2>
          <pre>{JSON.stringify(sessionData.sessionsByUser, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default SessionAnalytics;
