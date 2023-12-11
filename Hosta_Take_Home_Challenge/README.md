# Hosta take home assignment

## Overview
This project is centered around processing JSON files to update child-parent relationships based on data provided in a CSV file. The primary goal is to read JSON files, interpret a CSV file for object relationships, and update the JSON files accordingly, thereby enhancing data integrity and relationships within the dataset.

## Project Objectives and Delivery
* **Objective:** The core objective, as outlined in Task.md, was to establish a reliable method for updating JSON files with parent-child relationships derived from a CSV file. This involves parsing and interpreting structured data, ensuring accuracy in data manipulation, and maintaining data integrity throughout the process.
* **Delivery:** This project successfully delivers on these objectives by implementing a Python script that meticulously reads JSON and CSV files, accurately maps relationships from the CSV to the JSON objects, and updates the JSON files with new parent IDs. The script is designed to handle various challenges such as file encoding issues and complex data structures within the JSON files.

## Detailed Functionality
* **JSON File Processing:** The script reads JSON files, identifying each object and its attributes. It specifically looks for imageIds within each object to establish a connection with the CSV data.
* **CSV File Interpretation:** The CSV file is read to understand the relationships between objects. The script dynamically detects the file encoding for compatibility and processes each row to map Object_ID to Host_ID and Image IDs to unique object IDs.
* **Updating JSON Files:** Based on the mappings derived from the CSV file, the script updates each JSON file. It adds a `parent_id` to objects where a corresponding relationship is found, thereby enriching the JSON data with relational context.
* **Error Handling and Debugging:** The script includes error handling for file operations and prints informative messages for debugging and tracking the process flow.

## Files in the Project
- `3d3fde25-fc47-47ad-bda4-0b438196045b.json`: Original JSON file containing object data.
- `763fdd40-9408-45bb-b532-3f90b5c7c5d1.json`: Another original JSON file with object data.
- `b73070b3-7625-4975-872a-967b2297a458.json`: Third original JSON file with object data.
- `EXP_ObjectID_HostID.csv`: CSV file defining relationships between objects in JSON files.
- `update_json_relationships.py`: Python script to process JSON and CSV files.
- `Task.md`, `Task.pdf`: Documentation files with project requirements.

## Output Files
After running the script, the following updated JSON files are expected to be generated in the same directory:

- `updated_3d3fde25-fc47-47ad-bda4-0b438196045b.json`: Updated JSON file with new parent-child relationships.
- `updated_763fdd40-9408-45bb-b532-3f90b5c7c5d1.json`: Another updated JSON file with new parent-child relationships.
- `updated_b73070b3-7625-4975-872a-967b2297a458.json`: Third updated JSON file with new parent-child relationships.

These updated JSON files will reflect the enhanced data integrity and relationships as defined by the CSV file.

## Dependencies
- Python 3.x
- Standard libraries: `json`, `csv`
- python3 -m venv hosta
- source hosta/bin/activate

## How to Run the Script
- Ensure Python is installed on your system.
- Install required Python modules: Run ` pip3 install -r requirements.txt`
- Place `update_json_relationships.py` in the same directory as the JSON and CSV files.
- Open a terminal or command prompt.
- Navigate to the directory containing the script and files.
- Run the script: `python3 update_json_relationships.py`. This script will **run the pytest which includes unit test and integration test before generating the output files**.
- (Optionally) Test the script: `pytest test_update_json_relationships.py`
- Observe the console output for process information and any error messages.

## Meeting Project Expectations
- **Accuracy:** The script ensures high accuracy in data processing, as evidenced by the correct mapping of relationships and the addition of `parent_id` in the JSON files.
- **Efficiency:** The code is optimized for efficient processing, handling large files and complex data structures with ease.
- **Reliability:** Robust error handling and encoding detection make the script reliable for various file formats and data inconsistencies.
- **User Feedback:** Informative console messages provide users with clear insights into the script's process, aiding in debugging and verification.

## Author
Jimmy Malhan

## Date
12/10/2023
