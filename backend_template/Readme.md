# Running the Project

1. Activate your Python virtual environment (pyenv). If you haven't created one, create it using the following command:
`python -m venv myenv`

2. Activate your virtual environment with:
`source myenv/bin/activate`

3. Execute `chmod +x install_packages.sh` to make the Bash script executable.

4. Run `./install_packages.sh` to install or update required packages in your current virtual environment.

5. To update the list of installed packages, run `pip freeze > requirements.txt`.

This will set up your environment and update the package list.

## Installed Packages

- `anyio`: Asynchronous networking library
- `cffi`: C Foreign Function Interface for Python
- `click`: Command-line interface toolkit
- `fastapi`: A modern, fast, web framework for building APIs
- `h11`: HTTP/1.1 support
- `idna`: Internationalized domain names support
- `Jinja2`: Template engine
- `MarkupSafe`: Implements a text object that escapes characters for safe HTML rendering
- `passlib`: Password hashing library
- `psycopg2`: PostgreSQL database adapter
- `pycparser`: C parser and AST generator
- `pydantic`: Data validation and settings management
- `python-multipart`: Support for multipart file uploads
- `regex`: Regular expression operations
- `six`: Python 2 and 3 compatibility utilities
- `sniffio`: Sniff out which async library your code is running under
- `starlette`: Web framework toolkit
- `typing_extensions`: Backported and experimental type hints
- `uvicorn`: ASGI server
- `aiohttp`: Asynchronous HTTP client/server framework
- `redis`: Python client for Redis, a popular in-memory data store
- `celery`: Distributed task queue framework
- `gunicorn`: HTTP server for running Python web applications
- `Flask-Security`: Security extension for Flask web applications
- `SQLAlchemy`: SQL toolkit and Object-Relational Mapping (ORM) library for Python
