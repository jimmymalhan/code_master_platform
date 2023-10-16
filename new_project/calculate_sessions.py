
from collections import defaultdict
from itertools import groupby

# Function to calculate sessions
def calculate_sessions(sorted_events):
    sessions_by_user = defaultdict(list)

    for visitor_id, events in groupby(sorted_events, key=lambda x: x['visitorId']):
        events = list(events)
        current_session = {
            "duration": 0,
            "pages": [],
            "startTime": events[0]['timestamp']
        }
        
        for i, event in enumerate(events):
            timestamp = event["timestamp"]
            url = event["url"]
            
            if i == 0:
                current_session["pages"].append(url)
                continue

            time_diff = timestamp - current_session["startTime"]
            last_event_time = events[i - 1]['timestamp']
            
            # Check if the event should be part of the current session
            if timestamp - last_event_time <= 600000:  # 10 minutes in milliseconds
                current_session["duration"] = time_diff
                current_session["pages"].append(url)
            else:
                # Finalize the current session and start a new one
                sessions_by_user[visitor_id].append(current_session)
                current_session = {
                    "duration": 0,
                    "pages": [url],
                    "startTime": timestamp
                }
        
        # Add the last session
        sessions_by_user[visitor_id].append(current_session)
        
    return {"sessionsByUser": dict(sessions_by_user)}
