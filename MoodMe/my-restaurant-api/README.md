# Restaurant API Documentation

## Installation

Clone the repository and install dependencies:

git clone <repository-url>
cd my-restaurant-api
npm install

Start the server:

node server.js


## API Endpoints

### Get List of Restaurants

curl http://localhost:3000/
curl http://localhost:3000/api/restaurants
curl http://localhost:3000/api/search?name=Pizza
curl http://localhost:3000/api/search?cuisine=Italian&page=1&limit=5
curl "http://localhost:3000/api/search?address=Main+Street"



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
