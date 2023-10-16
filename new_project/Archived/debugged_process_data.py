
import json
from calculate_sessions import calculate_sessions  # Import the updated function
import requests

print("Starting the script...")

# API endpoint URL
api_url = "https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey=874713a5428a69b5b646581a25ba"

# Make the GET request
print("Fetching data from API...")
response = requests.get(api_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Successfully fetched data from API.")
    
    # Parse the JSON response
    actual_data = response.json()
    
    # Sort the events by visitorId and then by timestamp
    print("Sorting events...")
    sorted_events = sorted(actual_data['events'], key=lambda x: (x['visitorId'], x['timestamp']))
    
    # Calculate the sessions using the sorted events
    print("Calculating sessions...")
    calculated_sessions = calculate_sessions(sorted_events)

    print("Sessions calculated successfully.")
    
    # Here, you would send the calculated_sessions data to the API via HTTP POST
    # Uncomment the line below to send data
    # For example: requests.post(api_post_url, json=calculated_sessions)
else:
    print("Failed to fetch data from the API")
