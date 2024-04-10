const request = require('supertest');
const mongoose = require('mongoose');
const { MongoMemoryServer } = require('mongodb-memory-server');
const app = require('./server');

describe('API search functionality', () => {
  let mongoServer;

  beforeAll(async () => {
    // Ensure Mongoose is disconnected before starting a new in-memory server
    await mongoose.disconnect();

    mongoServer = await MongoMemoryServer.create();
    const mongoUri = mongoServer.getUri();
    await mongoose.connect(mongoUri, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
  });

  afterAll(async () => {
    await mongoose.disconnect();
    await mongoServer.stop();
  });

  test('GET /api/search with no parameters returns all restaurants', async () => {
    const response = await request(app).get('/api/search');
    expect(response.statusCode).toBe(200);
    expect(response.body).toBeInstanceOf(Array);
  });

  test('GET /api/search with name parameter', async () => {
    const response = await request(app).get('/api/search?name=Pizza');
    expect(response.statusCode).toBe(200);
  });
});
