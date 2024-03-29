const mongoose = require('mongoose');
const fs = require('fs');
const path = require('path');

// Update the path to where your Restaurant model is located relative to this script
const Restaurant = require('./restaurantModel');

const filePath = path.join(__dirname, 'restaurants.json'); // Update if necessary

mongoose.connect('mongodb://localhost:27017/myRestaurantDB', { useNewUrlParser: true, useUnifiedTopology: true });

mongoose.connection.once('open', () => {
    console.log('Connected to MongoDB');
    fs.readFile(filePath, { encoding: 'utf-8' }, (err, data) => {
        if (err) {
            console.error('Error reading file:', err);
            return;
        }
        const restaurants = JSON.parse(data);
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
