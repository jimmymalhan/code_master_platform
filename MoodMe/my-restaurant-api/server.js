require('dotenv').config();
const express = require('express');
const mongoose = require('mongoose');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(express.json());

// MongoDB connection - Updated to connect locally
const mongoDBUri = 'mongodb://localhost:27017/myLocalDB'; // Update this line
mongoose.connect(mongoDBUri, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Connected to MongoDB locally'))
  .catch(err => console.error('Could not connect to MongoDB', err));

// Sample API endpoint
app.get('/api/restaurants', (req, res) => {
  // This will be replaced with actual database interaction
  res.send('List of restaurants');
});

app.listen(PORT, () => console.log(`Server running on http://localhost:${PORT}`));
