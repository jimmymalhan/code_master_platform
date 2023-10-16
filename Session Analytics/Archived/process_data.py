
import json
from calculate_sessions import calculate_sessions  # Import the updated function
import requests

# API endpoint URL
api_url = "https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey=874713a5428a69b5b646581a25ba"

# Make the GET request
response = requests.get(api_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    actual_data = response.json()
    
    # Sort the events by visitorId and then by timestamp
    sorted_events = sorted(actual_data['events'], key=lambda x: (x['visitorId'], x['timestamp']))
    
    # Calculate the sessions using the sorted events
    calculated_sessions = calculate_sessions(sorted_events)

    # Here, you would send the calculated_sessions data to the API via HTTP POST
    # For example: requests.post(api_post_url, json=calculated_sessions)
else:
    print("Failed to fetch data from the API")


# Load the calculated sessions from the JSON file
with open('calculated_sessions.json', 'r') as file:
    calculated_sessions = json.load(file)

# API endpoint for POST
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
