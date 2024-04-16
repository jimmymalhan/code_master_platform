# activate virtual environment
source salesbricks/bin/activate

start postgres

psql -U jimmy -d postgres



### Folder Structure
├── db/
│   ├── __init__.py
│   ├── database_setup.py       # SQL table creation and DB connection setup
│   └── models.py               # ORM models, if you choose to use an ORM
│
├── services/
│   ├── __init__.py
│   ├── event_processor.py      # Logic to handle and process events
│   └── data_aggregator.py      # Logic for data aggregation and analysis
│
├── api/
│   ├── __init__.py
│   ├── routes.py               # API routes for interacting with the front-end
│   └── controllers.py          # API logic to handle requests and send responses
│
├── tests/
│   ├── __init__.py
│   ├── test_database.py        # Tests for database operations
│   ├── test_services.py        # Tests for service logic
│   └── test_api.py             # Tests for API endpoints
│
├── static/
│   └── (static files like JS, CSS, images for your dashboard if applicable)
│
├── templates/
│   └── (HTML templates if serving pages directly)
│
├── utils/
│   ├── __init__.py
│   └── helpers.py              # Utility functions and helpers
│
├── config.py                   # Configuration settings (DB creds, API keys, etc.)
├── main.py                     # Entry point of the application
└── requirements.txt            # Python package dependencies