# Running the Project

1. Activate your Python virtual environment (pyenv). If you haven't created one, create it using the following command:
    ```bash
    python -m venv myenv
    ```

2. Activate your virtual environment with:
    ```bash
    source myenv/bin/activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. To update the list of installed packages, run:
    ```bash
    pip freeze > requirements.txt
    ```

This will set up your environment and update the package list.

## What Happens When You Run `run_all.py`:

1. It fetches raw event data from an API.
2. It sorts the events by visitorId and timestamp.
3. It calls the SessionCalculator class from `calculate_sessions.py` to calculate the sessions based on the sorted events.
4. It saves the calculated sessions to a JSON file named `calculated_sessions.json`.
5. It sends the calculated session data back to an API via an HTTP POST request.

---

# Analytics Sessions Project

## Table of Contents
1. [Main Files](#main-files)
    - [calculate_sessions.py](#calculate_sessionspy)
    - [calculated_sessions.json](#calculated_sessionsjson)
    - [run_all.py](#run_allpy)
2. [Archived or Unused Files](#archived-or-unused-files)
    - [debugged_process_data.py](#debugged_process_datapy)
    - [process_data.py](#process_datapy)
    - [save_json_process_data.py](#save_json_process_datapy)
    - [validation_script.py](#validation_scriptpy)
3. [FAQ](#faq)

---

## Main Files

### calculate_sessions.py
- **Purpose**: This is where the core logic for calculating the sessions resides.
- **What it does**: 
  - Imports necessary libraries.
  - Defines the function `calculate_sessions` that takes the event data and calculates sessions based on your criteria.

---

### calculated_sessions.json
- **Purpose**: This JSON file holds the output data—the calculated sessions.
- **What it does**: 
  - Stores the session data in a JSON format that can be easily used or sent to an API.

---

### run_all.py
- **Purpose**: This is your all-in-one script.
- **What it does**: 
  - Fetches data from the API.
  - Calculates the sessions.
  - Sends the calculated sessions to the API via a POST request.

---

## Archived or Unused Files

### debugged_process_data.py
- **Purpose**: A debug version of `process_data.py`.
- **What it does**: 
  - Fetches data from the API.
  - Includes debug statements or tweaks for troubleshooting.

---

### process_data.py
- **Purpose**: Fetches raw data from the API and calculates sessions.
- **What it does**: 
  - Makes a GET request for data.
  - Calls `calculate_sessions` to calculate sessions.

---

### save_json_process_data.py
- **Purpose**: A variant of `process_data.py` that saves output to JSON.
- **What it does**: 
  - Fetches data.
  - Calculates sessions.
  - Saves sessions to `calculated_sessions.json`.

---

### validation_script.py
- **Purpose**: Validates the calculated sessions.
- **What it does**: 
  - Loads `calculated_sessions.json`.
  - Validates data.
  - Prints a validation message.

---

## FAQ

### What is the purpose of this project?
This project is designed to calculate web analytics sessions based on provided event data.

### How do I run the project?
Follow the steps under "Running the Project" to set up your environment and execute the scripts.

### What are the main files I should focus on?
You should mainly focus on `calculate_sessions.py`, `calculated_sessions.json`, and `run_all.py`. These contain the core logic and results.

### Why are there archived or unused files?
These files were part of the development process and are kept for historical or troubleshooting purposes. Feel free to ignore them.

