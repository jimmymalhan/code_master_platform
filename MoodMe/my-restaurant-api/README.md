# Restaurant API Documentation

## Installation

Clone the repository and install dependencies:

git clone <repository-url>
cd my-restaurant-api
npm install

Start the server:

npm start


## API Endpoints

### Get List of Restaurants

- **GET** `/api/restaurants`

Returns a list of restaurants.

## Usage

Use Postman or any HTTP client to make requests to the API.

Example request:
GET http://localhost:3000/api/restaurants


Example response:

```json
[
  {
    "name": "Restaurant Name",
    "cuisine": "Cuisine Type",
    "address": {
      "street": "Street Name",
      "building": "Building Number"
    }
  }
]
