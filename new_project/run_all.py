
import json
from calculate_sessions import calculate_sessions
import requests

print("Fetching data from API...")

# API endpoint URL for GET
api_url = "https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey=874713a5428a69b5b646581a25ba"

# Make the GET request
response = requests.get(api_url)

# Check if the GET request was successful (status code 200)
if response.status_code == 200:
    print("Successfully fetched data from API.")
    
    # Parse the JSON response
    actual_data = response.json()
    
    # Sort the events by visitorId and timestamp
    sorted_events = sorted(actual_data['events'], key=lambda x: (x['visitorId'], x['timestamp']))
    
    # Calculate the sessions
    calculated_sessions = calculate_sessions(sorted_events)
    
    # Save to JSON file (Optional)
    with open("calculated_sessions.json", "w") as json_file:
        json.dump(calculated_sessions, json_file, indent=4)
    
    print("Calculated sessions and saved to calculated_sessions.json.")
    
    # API endpoint URL for POST
    api_post_url = "https://candidate.hubteam.com/candidateTest/v3/problem/result?userKey=874713a5428a69b5b646581a25ba"
    
    # Make the POST request
    response = requests.post(api_post_url, json=calculated_sessions)
    
    # Check the response
    if response.status_code == 200:
        print("Successfully sent data to API. Received 200 OK.")
    elif response.status_code == 400:
        print("Failed to send data. Received 400. Response message:", response.json())
    else:
        print("Received unexpected status code:", response.status_code)
else:
    print("Failed to fetch data from the API")
