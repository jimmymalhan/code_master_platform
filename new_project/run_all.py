import json
import requests
from calculate_sessions import SessionCalculator

class SessionProcessor:
    def __init__(self, api_key):
        self.api_key = api_key

    def fetch_data_from_api(self):
        api_url = f"https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey={self.api_key}"
        response = requests.get(api_url)
        return response.json()

    def calculate_and_post_sessions(self):
        data = self.fetch_data_from_api()

        if data:
            events = data['events']
            calculator = SessionCalculator(events)
            calculated_sessions = calculator.calculate_sessions()

            if calculated_sessions:
                self.save_sessions_to_json(calculated_sessions)
                self.post_sessions_to_api(calculated_sessions)

    def save_sessions_to_json(self, sessions):
        with open("calculated_sessions.json", "w") as json_file:
            json.dump(sessions, json_file, indent=4)

    def post_sessions_to_api(self, sessions):
        api_post_url = f"https://candidate.hubteam.com/candidateTest/v3/problem/result?userKey={self.api_key}"
        response = requests.post(api_post_url, json=sessions)

        if response.status_code == 200:
            print("Successfully sent data to API. Received 200 OK.")
        elif response.status_code == 400:
            print("Failed to send data. Received 400. Response message:", response.json())
        else:
            print("Received unexpected status code:", response.status_code)

if __name__ == "__main__":
    api_key = "874713a5428a69b5b646581a25ba"
    processor = SessionProcessor(api_key)
    processor.calculate_and_post_sessions()
