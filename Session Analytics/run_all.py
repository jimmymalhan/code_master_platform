import json
import requests
import unittest
from calculate_sessions import calculate_sessions

# Function to fetch data from the API
def fetch_data(api_url):
    response = requests.get(api_url)
    return response

# Function to send data to the API
def send_data(api_url, data):
    response = requests.post(api_url, json=data)
    return response

# Function to process data, calculate sessions, and send results to the API
def main():
    print("Fetching data from API...")
    api_url = "https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey=874713a5428a69b5b646581a25ba"
    response = fetch_data(api_url)

    if response.status_code == 200:
        print("Successfully fetched data from API.")
        
        actual_data = response.json()
        sorted_events = sorted(actual_data['events'], key=lambda x: (x['visitorId'], x['timestamp']))
        
        calculated_sessions = calculate_sessions(sorted_events)
        
        with open("calculated_sessions.json", "w") as json_file:
            json.dump(calculated_sessions, json_file, indent=4)
        
        print("Calculated sessions and saved to calculated_sessions.json.")
        
        api_post_url = "https://candidate.hubteam.com/candidateTest/v3/problem/result?userKey=874713a5428a69b5b646581a25ba"
        response = send_data(api_post_url, calculated_sessions)
        
        if response.status_code == 200:
            print("Successfully sent data to API. Received 200 OK.")
        elif response.status_code == 400:
            print("Failed to send data. Received 400. Response message:", response.json())
        else:
            print("Received unexpected status code:", response.status_code)
    else:
        print("Failed to fetch data from the API")

# Entry point of the script
if __name__ == "__main__":
    main()

# Unit Tests
class TestRunAll(unittest.TestCase):
    def test_fetch_data(self):
        api_url = "https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey=874713a5428a69b5b646581a25ba"
        response = fetch_data(api_url)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
