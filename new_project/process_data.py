import json
from calculate_sessions import calculate_sessions
import requests

# API endpoint URL
api_url = "https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey=874713a5428a69b5b646581a25ba"

# Make the GET request
response = requests.get(api_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    actual_data = response.json()

    # Save the actual_data to a JSON file
    with open("actual_data.json", "w") as json_file:
        json.dump(actual_data, json_file, indent=4)

    # Now you have the actual data, replace raw_data with actual_data in your process_data.py script
else:
    print("Failed to fetch data from the API")
