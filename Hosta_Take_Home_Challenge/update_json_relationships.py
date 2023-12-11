"""
update_json_relationships.py

This script updates child-parent relationships in JSON files based on data provided in a CSV file.
Tasks:
1. Read and process JSON files to identify objects and their attributes.
2. Read and interpret the CSV file to understand object relationships.
3. Update JSON files with correct parent IDs based on CSV data.
4. Ensure the code is reusable and well-documented.

Author: [Your Name]
Date: [Date]
"""

import json
import csv

class JSONFileHandler:
    """
    Handles operations related to JSON file processing.
    """
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = self.read_json()

    def read_json(self):
        # Read JSON file and return data
        try:
            with open(self.filepath, 'r') as file:
                return json.load(file)
        except IOError as e:
            print(f"Error reading file {self.filepath}: {e}")
            return None

    def update_relationships(self, parent_mapping, image_id_mapping):
        """
        Update the JSON data with new parent-child relationships.
        :param parent_mapping: Dictionary with child IDs as keys and parent IDs as values.
        :param image_id_mapping: Dictionary mapping image IDs to unique object IDs.
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
        # Save the updated JSON data to a new file
        try:
            with open(new_filepath, 'w') as file:
                json.dump(self.data, file, indent=4)
        except IOError as e:
            print(f"Error writing file {new_filepath}: {e}")

class CSVFileHandler:
    """
    Handles operations related to CSV file processing.
    """
    def __init__(self, filepath):
        self.filepath = filepath

    def read_csv(self):
        # Read CSV file and return data
        try:
            with open(self.filepath, newline='', encoding='utf-8-sig') as csvfile:  # Adjusted for potential UTF encoding with BOM
                return list(csv.DictReader(csvfile))
        except IOError as e:
            print(f"Error reading file {self.filepath}: {e}")
            return []

def find_parent_child_relationships(csv_data):
    """
    Analyze CSV data to find parent-child relationships.
    Returns two dictionaries: one mapping child IDs to parent IDs, and another mapping image IDs to unique object IDs.
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

def main():
    # Main function to orchestrate the updating process
    json_file_paths = [
        '3d3fde25-fc47-47ad-bda4-0b438196045b.json',
        '763fdd40-9408-45bb-b532-3f90b5c7c5d1.json',
        'b73070b3-7625-4975-872a-967b2297a458.json'
    ]  # List of JSON file paths
    csv_file_path = 'EXP_ObjectID_HostID.csv'  # Path to the CSV file

    csv_handler = CSVFileHandler(csv_file_path)
    csv_data = csv_handler.read_csv()
    relationships = find_parent_child_relationships(csv_data)

    for json_path in json_file_paths:
        json_handler = JSONFileHandler(json_path)
        if json_handler.data and csv_data:
            updated = json_handler.update_relationships(relationships)
            if updated:
                new_json_path = f"updated_{json_path}"  # Naming the new file
                json_handler.save_json(new_json_path)
                print(f"Updated JSON file saved as {new_json_path}.")
            else:
                print(f"No updates were made to the JSON file {json_path}.")
        else:
            print(f"Failed to read data from {json_path} or CSV file.")

if __name__ == "__main__":
    main()
