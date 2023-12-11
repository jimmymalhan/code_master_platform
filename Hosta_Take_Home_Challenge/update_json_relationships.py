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
            print(f"Error reading file {self.filepath}: {e}")
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
            print(f"Updated JSON file saved as {new_filepath}.")
        except IOError as e:
            print(f"Error writing file {new_filepath}: {e}")

class CSVFileHandler:
    def __init__(self, filepath):
        self.filepath = filepath

    def read_csv(self):
        # Detect the encoding of the CSV file
        encoding = self.detect_encoding()
        if encoding is None:
            print(f"Failed to detect encoding for file {self.filepath}")
            return []

        try:
            with open(self.filepath, newline='', encoding=encoding) as csvfile:
                csv_reader = csv.DictReader(csvfile, delimiter='\t')  # Adjust delimiter if necessary
                return list(csv_reader)
        except IOError as e:
            print(f"Error reading file {self.filepath}: {e}")
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
            print(f"Error reading file {self.filepath}: {e}")
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

    # Debugging: Print the mappings
    print("Parent Mapping:", parent_mapping)
    print("Image ID Mapping:", image_id_mapping)

    return parent_mapping, image_id_mapping

def process_json_file(json_path, parent_mapping, image_id_mapping):
    """
    Function to process each JSON file in a separate thread.
    """
    json_handler = JSONFileHandler(json_path)
    if json_handler.data:
        new_json_path = f"updated_{json_path}"
        if json_handler.update_relationships(parent_mapping, image_id_mapping):
            json_handler.save_json(new_json_path)
        else:
            print(f"No updates were made to the JSON file {json_path}.")
    else:
        print(f"Failed to read data from {json_path}.")

def main():
    csv_file_path = 'EXP_ObjectID_HostID.csv'
    csv_handler = CSVFileHandler(csv_file_path)
    csv_data = csv_handler.read_csv()
    parent_mapping, image_id_mapping = find_parent_child_relationships(csv_data)

    json_file_paths = [
        '3d3fde25-fc47-47ad-bda4-0b438196045b.json',
        '763fdd40-9408-45bb-b532-3f90b5c7c5d1.json',
        'b73070b3-7625-4975-872a-967b2297a458.json'
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_json_file, path, parent_mapping, image_id_mapping) for path in json_file_paths]
        for future in concurrent.futures.as_completed(futures):
            future.result()  # This will raise exceptions from threads, if any

if __name__ == "__main__":
    main()
