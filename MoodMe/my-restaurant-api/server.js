// Import the required modules
require('dotenv').config();

const express = require('express');
const mongoose = require('mongoose');
const Restaurant = require('./restaurantModel'); // Adjust this path as needed

// Initialize the express app
const app = express();

// Serve static files from the public directory
app.use(express.static('public'));

// Middleware to parse JSON bodies
app.use(express.json());

// Connect to MongoDB with updated connection options
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
}).then(() => console.log('Connected to MongoDB'))
  .catch(err => console.error('Could not connect to MongoDB...', err));

// API endpoint to get all restaurants from MongoDB
app.get('/api/restaurants', async (req, res) => {
  try {
    const restaurants = await Restaurant.find();
    res.json(restaurants);
  } catch (error) {
    res.status(500).send(error.message);
  }
});

// REST API endpoint /search for restaurant searches with query parameters and pagination
app.get('/api/search', async (req, res) => {
  const { name, cuisine, address, page = 1, limit = 10 } = req.query;
  try {
    const query = {};
    if (name) query.name = { $regex: name, $options: 'i' };
    if (cuisine) query.cuisine = { $regex: cuisine, $options: 'i' };
    if (address) query["address.street"] = { $regex: address, $options: 'i' };
    const restaurants = await Restaurant.find(query).skip((page - 1) * limit).limit(parseInt(limit));
    res.json(restaurants);
    console.log('Executing query:', query);
  } catch (error) {
    console.error('Search error:', error);
    res.status(500).send(error.message);
  }
});

// Welcome route should now correctly display static files or the welcome message as a fallback
app.get('/', (req, res) => {
  res.send('Welcome to the Restaurant API!');
});

// Start the server and listen on the specified PORT only if not in test mode
const PORT = process.env.PORT || 3000;
if (process.env.NODE_ENV !== 'test') {
  app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
  });
}

module.exports = app; // Export the Express app for testing purposes
