#!/bin/bash

# List of packages to install
packages=(
  "anyio==3.7.0"
  "cffi==1.15.1"
  "click==8.1.3"
  "fastapi==0.99.0"
  "h11==0.14.0"
  "idna==3.4"
  "Jinja2==3.1.2"
  "MarkupSafe==2.1.3"
  "passlib==1.7.4"
  "psycopg2==2.9.6"
  "pycparser==2.21"
  "pydantic==1.10.10"
  "python-multipart==0.0.6"
  "regex==2023.6.3"
  "six==1.16.0"
  "sniffio==1.3.0"
  "starlette==0.27.0"
  "typing_extensions==4.7.0"
  "uvicorn==0.22.0"
  "aiohttp==3.8.1"
  "redis==4.0.2"
  "celery==5.2.1"
  "gunicorn==20.1.0"
  "Flask-Security==4.0.1"
  "SQLAlchemy==1.4.25"
)

# Loop through each package and install it
for pkg in "${packages[@]}"; do
  echo "Installing $pkg..."
  pip install $pkg
done

echo "All packages installed!"
