// Import the required modules
require('dotenv').config();
const express = require('express');
const mongoose = require('mongoose');
const fs = require('fs');

// Initialize the express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(express.json());

// Connect to MongoDB
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: false,
  useUnifiedTopology: false,
});

// Load restaurant data from JSON file
const restaurantData = JSON.parse(fs.readFileSync('restaurants.json', 'utf8'));

// API endpoint to get restaurants
app.get('/api/restaurants', (req, res) => {
  res.json(restaurantData);
});

// Welcome route for the root path
app.get('/', (req, res) => {
  res.send('Welcome to the Restaurant API!');
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});