// Import the required modules
require('dotenv').config();
const express = require('express');
const mongoose = require('mongoose');
const Restaurant = require('./restaurantModel'); // Ensure this path matches your Restaurant model

// Initialize the express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON bodies
app.use(express.json());

// Connect to MongoDB with updated connection options
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true, // Use the new URL parser
  useUnifiedTopology: true, // Use the new server discovery and monitoring engine
  // useCreateIndex: true, // Use MongoDB's new method to ensure index creation
  // useFindAndModify: false, // Use MongoDB's findOneAndUpdate() without deprecation warnings
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

// Define a REST API endpoint /search for restaurant searches with query parameters and pagination
app.get('/api/search', async (req, res) => {
  const { name, cuisine, address, page = 1, limit = 10 } = req.query;

  try {
    const query = {};

    // Construct query based on request parameters
    if (name) query.name = { $regex: name, $options: 'i' };
    if (cuisine) query.cuisine = { $regex: cuisine, $options: 'i' };
    if (address) query["address.street"] = { $regex: address, $options: 'i' };

    // Fetch data with pagination
    const restaurants = await Restaurant.find(query)
      .skip((page - 1) * limit)
      .limit(parseInt(limit)); // Ensure limit is an integer
      res.json(restaurants);


    // Diagnostic: Log query to see what's being executed
    console.log('Executing query:', query);

  } catch (error) {
    console.error('Search error:', error); // Added console error for diagnostics
    res.status(500).send(error.message);
  }
});

// Welcome route for the root path
app.get('/', (req, res) => {
  res.send('Welcome to the Restaurant API!');
});

// Start the server and listen on the specified PORT
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
