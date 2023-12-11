"""
update_json_relationships.py

This script updates child-parent relationships in JSON files based on data provided in a CSV file.
Tasks:
1. Read and process JSON files to identify objects and their attributes.
2. Read and interpret the CSV file to understand object relationships.
3. Update JSON files with correct parent IDs based on CSV data.
4. Ensure the code is reusable and well-documented.

Author: Jimmy Malhan
Date: 12/10/2023
"""

import json
import csv
import concurrent.futures
import logging
import chardet
import os
import subprocess
import sys

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
class JSONFileHandler:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = self.read_json()

    def read_json(self):
        """
        Read a JSON file and return its contents as a dictionary.
        Handles IOError if file reading fails.
        """
        try:
            with open(self.filepath, 'r') as file:
                return json.load(file)
        except IOError as e:
            logging.error(f"Error reading file {self.filepath}: {e}")
            return None

    def update_relationships(self, parent_mapping, image_id_mapping):
        """
        Update JSON data with new parent-child relationships.
        :param parent_mapping: Dictionary with child IDs as keys and parent IDs as values.
        :param image_id_mapping: Dictionary mapping image IDs to unique object IDs.
        :return: True if updates were made, False otherwise.
        """
        updated = False
        for obj in self.data.get('ops_3d', []):
            image_ids = obj.get('imageIds', [])
            for image_id in image_ids:
                if image_id in image_id_mapping:
                    unique_id = image_id_mapping[image_id]
                    if unique_id in parent_mapping:
                        obj['parent_id'] = parent_mapping[unique_id]
                        updated = True
        return updated

    def save_json(self, new_filepath):
        """
        Save the updated JSON data to a new file.
        :param new_filepath: Path to the new JSON file.
        """
        try:
            with open(new_filepath, 'w') as file:
                json.dump(self.data, file, indent=4)
            logging.info(f"Updated JSON file saved as {new_filepath}.")
        except IOError as e:
            logging.error(f"Error writing file {new_filepath}: {e}")

class CSVFileHandler:
    def __init__(self, filepath):
        self.filepath = filepath

    def read_csv(self):
        # Detect the encoding of the CSV file
        encoding = self.detect_encoding()
        if encoding is None:
            logging.error(f"Failed to detect encoding for file {self.filepath}")
            return []

        try:
            with open(self.filepath, newline='', encoding=encoding) as csvfile:
                csv_reader = csv.DictReader(csvfile, delimiter='\t')  # Adjust delimiter if necessary
                return list(csv_reader)
        except IOError as e:
            logging.error(f"Error reading file {self.filepath}: {e}")
            return []

    def detect_encoding(self):
        try:
            with open(self.filepath, 'rb') as file:
                detector = chardet.universaldetector.UniversalDetector()
                for line in file:
                    detector.feed(line)
                    if detector.done:
                        break
                detector.close()
                return detector.result['encoding']
        except IOError as e:
            logging.error(f"Error reading file {self.filepath}: {e}")
            return None

def find_parent_child_relationships(csv_data):
    """
    Analyze CSV data to find parent-child relationships.
    Returns two dictionaries: one mapping child IDs to parent IDs, and another mapping image IDs to unique object IDs.
    :param csv_data: List of dictionaries representing CSV data.
    :return: Tuple of dictionaries (parent_mapping, image_id_mapping).
    """
    parent_mapping = {}
    image_id_mapping = {}
    for row in csv_data:
        object_id = row.get('Object_ID')
        host_id = row.get('Host_ID')
        if object_id and host_id:
            parent_mapping[object_id] = host_id
        for key, value in row.items():
            if 'Image' in key and value:
                image_id_mapping[value] = object_id

    return parent_mapping, image_id_mapping

def process_json_file(json_path, parent_mapping, image_id_mapping):
    """
    Function to process each JSON file in a separate thread.
    """
    json_handler = JSONFileHandler(json_path)
    if json_handler.data:
        # Extract the original filename without extension
        original_filename = os.path.splitext(os.path.basename(json_path))[0]

        # Customize the new filename format as needed
        new_filename = f"updated_{original_filename}.json"

        new_json_path = os.path.join(os.path.dirname(json_path), new_filename)

        if json_handler.update_relationships(parent_mapping, image_id_mapping):
            json_handler.save_json(new_json_path)
        else:
            print(f"No updates were made to the JSON file {json_path}.")
    else:
        print(f"Failed to read data from {json_path}.")

def run_tests():
    """
    Run the test script using pytest.
    """
    test_command = "pytest test_update_json_relationships.py"
    test_result = subprocess.call(test_command, shell=True)
    if test_result != 0:
        logging.error("Test failed. Exiting.")
        sys.exit(1)
    else:
        logging.info("Test passed. Proceeding with data processing.")


def main():
    # Run the test script before proceeding
    run_tests()

    # Specify the correct CSV file name
    csv_filename = 'EXP_ObjectID_HostID.csv'  # Update with the correct CSV file name

    # Build the full path to the CSV file
    csv_path = os.path.join('.', csv_filename)

    csv_handler = CSVFileHandler(csv_path)
    csv_data = csv_handler.read_csv()
    if not csv_data:
        logging.error("No CSV data found. Exiting.")
        sys.exit(1)

    parent_mapping, image_id_mapping = find_parent_child_relationships(csv_data)

    # Assuming JSON files are listed in a directory
    json_files = [file for file in os.listdir('.') if file.endswith('.json')]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_json_file, file, parent_mapping, image_id_mapping) for file in json_files]
        for future in concurrent.futures.as_completed(futures):
            future.result()

if __name__ == "__main__":
    main()