import axios from 'axios';

// Define a function to fetch the JSON data
export async function fetchCalculatedSessions() {
  try {
    const response = await axios.get('/api/calculated_sessions.json'); // Updated API endpoint
    return response.data;
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }
}
