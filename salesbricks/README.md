# SalesBricks Project

## Project Overview

SalesBricks is a Python-based Software as a Service (SaaS) application designed for real-time reporting on subscription services. It enables functionalities for forecasting and visualizing revenue, tracking subscription states, and processing events in real time.

## Main Features

### 1. Set Up Backend Infrastructure

- Selected a web framework: FastAPI
- Decided on a real-time data handling mechanism: WebSocket for real-time updates
- Chose a database: SQLite for its JSON handling and robustness

### 2. Develop Event Handling System

- Implemented listeners for event types (ORDER_CLOSED_WON, ORDER_CLOSED_WON_REVENUE, etc.)
- Processed and transformed these events into actionable data insights and real-time updates

### 3. Create Data Visualization Interface

- Developed endpoints for fetching real-time data
- Integrated a frontend library (e.g., Chart.js) to visualize data as required

### 4. Implement Filtering Capability

- Allowed data querying by date range, buyer, and product
- Ensured this is optimized for performance to meet the requirement of fast load times

## Setup Instructions

### Prerequisites

Ensure you have the following installed:

- Python 3.8 or higher
- `pip` and `virtualenv`

### Setting Up the Local Development Environment

Clone the repository and set up a virtual environment:

```bash
git clone <https://github.com/jimmymalhan/code_master_platform/>
cd salesbricks
```

### Create and activate a virtual environment

```bash
python3 -m venv salesbricks-venv
source salesbricks-venv/bin/activate
```

### Install dependencies

```bash
pip3 install -r requirements.txt
```

### Initialize the Database

Before starting the application, initialize the database:

```bash
python3 -c 'from app.db import init_db; init_db()'
```

### Running the Application

Launch the application using uvicorn with live reload enabled for development:

```bash
uvicorn app.main:app --reload
```

### Available Endpoints

You can access the application and its documentation at the following URLs:

- API documentation (Swagger UI): <http://127.0.0.1:8000/docs>
- Home: <http://127.0.0.1:8000/>
- Subscriptions API: <http://127.0.0.1:8000/subscriptions>
- Orders API: <http://127.0.0.1:8000/orders>
- Close Order: <http://127.0.0.1:8000/close-order/{order_id}> (POST method)
- Record Revenue: <http://127.0.0.1:8000/record-revenue/{order_id}/{revenue}> (POST method)
- Monthly Data: <http://127.0.0.1:8000/data> (GET method)

### If you need to identify and stop the server running on a specific port

```bash
lsof -i :<8000>
kill -9 <PID>
```

### Running Tests

Navigate to the tests directory and run the tests to ensure everything is set up correctly:

```bash
cd tests
pytest
```

Ensure that all tests pass to verify that your setup was successful.

### Updating Dependencies

If you install any new packages during development, update the requirements.txt file:

```bash
pip3 freeze > requirements.txt
```
