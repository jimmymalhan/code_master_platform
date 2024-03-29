const mongoose = require('mongoose');

// Define the schema for the restaurant data
const restaurantSchema = new mongoose.Schema({
  _id: mongoose.Schema.Types.ObjectId,
  address: {
    building: String,
    street: String,
    zipcode: String, // If your data includes a zipcode, add this line. Otherwise, omit it.
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

// Create the model from the schema
const Restaurant = mongoose.model('Restaurant', restaurantSchema);

module.exports = Restaurant;
