const mongoose = require('mongoose');
const fs = require('fs');
const path = require('path');
const Restaurant = require('./restaurantModel');

const filePath = path.join(__dirname, 'restaurants.json');

mongoose.connect('mongodb://localhost:27017/myRestaurantDB', {
  useNewUrlParser: true,
  useUnifiedTopology: true
});

mongoose.connection.once('open', () => {
  console.log('Connected to MongoDB');
  fs.readFile(filePath, { encoding: 'utf-8' }, (err, data) => {
    if (err) {
      console.error('Error reading file:', err);
      return;
    }

    // Parse JSON data
    let restaurants = JSON.parse(data);

    // Transform data
    restaurants = restaurants.map(restaurant => {
      // Correctly instantiate a new ObjectId
      restaurant._id = new mongoose.Types.ObjectId(restaurant._id.$oid);

      // Convert dates in grades
      restaurant.grades = restaurant.grades.map(grade => {
        grade.date = new Date(grade.date.$date);
        return grade;
      });

      return restaurant;
    });

    // Insert transformed data
    Restaurant.insertMany(restaurants)
      .then(() => {
        console.log('Data imported successfully');
        mongoose.connection.close();
      })
      .catch((error) => {
        console.error('Error importing data:', error);
        mongoose.connection.close();
      });
  });
});
