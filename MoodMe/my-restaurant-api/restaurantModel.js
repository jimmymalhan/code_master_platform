const mongoose = require('mongoose');

// Define the schema for the restaurant data
const restaurantSchema = new mongoose.Schema({
  _id: mongoose.Schema.Types.ObjectId,
  address: {
    building: String,
    street: String,
    // zipcode: String, // Include or omit based on your data structure and requirements.
  },
  cuisine: String,
  grades: [{
    date: Date,
    grade: String,
    score: Number
  }],
  name: String,
  restaurant_id: String
});

// Add indexes to optimize query performance for frequently searched fields
restaurantSchema.index({ name: 'text', cuisine: 'text', 'address.street': 'text' });

// Create the model from the schema
const Restaurant = mongoose.model('Restaurant', restaurantSchema);

module.exports = Restaurant;
