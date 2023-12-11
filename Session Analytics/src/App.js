import React, { useState, useEffect } from 'react';
import './App.css'; // Make sure the path matches the location of your CSS file
import { fetchCalculatedSessions } from './api'; // Updated the import path

function App() {
  const [sessions, setSessions] = useState([]);

  useEffect(() => {
    async function fetchData() {
      try {
        const response = await fetchCalculatedSessions(); // Use your API endpoint here
        if (response.ok) {
          const data = await response.json();
          setSessions(data.sessionsByUser);
        } else {
          console.error('Failed to fetch data');
        }
      } catch (error) {
        console.error('An error occurred:', error);
      }
    }

    fetchData();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Welcome to My React App</h1>
        <p>This is the App component.</p>
        <h2>Calculated Sessions:</h2>
        <pre>{JSON.stringify(sessions, null, 2)}</pre>
      </header>
    </div>
  );
}

export default App;
