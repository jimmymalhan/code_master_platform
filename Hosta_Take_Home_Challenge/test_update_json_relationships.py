import pytest
from update_json_relationships import JSONFileHandler, CSVFileHandler, find_parent_child_relationships

# Test JSONFileHandler for each JSON file
@pytest.mark.parametrize("json_file", [
    "3d3fde25-fc47-47ad-bda4-0b438196045b.json",
    "763fdd40-9408-45bb-b532-3f90b5c7c5d1.json",
    "b73070b3-7625-4975-872a-967b2297a458.json",
])
def test_read_json(json_file):
    handler = JSONFileHandler(json_file)
    assert handler.data is not None, f"Failed to read JSON file: {json_file}"

# Test CSVFileHandler for the CSV file
def test_read_csv():
    csv_file = "EXP_ObjectID_HostID.csv"
    handler = CSVFileHandler(csv_file)
    csv_data = handler.read_csv()
    assert isinstance(csv_data, list), f"Failed to read CSV file: {csv_file}"

# Sample integration test for each JSON file and the CSV file
@pytest.mark.parametrize("json_file", [
    "3d3fde25-fc47-47ad-bda4-0b438196045b.json",
    "763fdd40-9408-45bb-b532-3f90b5c7c5d1.json",
    "b73070b3-7625-4975-872a-967b2297a458.json",
])
def test_end_to_end(json_file):
    # End-to-end test of the entire process for each JSON file
    csv_file = "EXP_ObjectID_HostID.csv"
    csv_handler = CSVFileHandler(csv_file)
    csv_data = csv_handler.read_csv()
    parent_mapping, image_id_mapping = find_parent_child_relationships(csv_data)

    json_handler = JSONFileHandler(json_file)
    updated = json_handler.update_relationships(parent_mapping, image_id_mapping)
    assert updated, f"End-to-end test failed for JSON file: {json_file}"

