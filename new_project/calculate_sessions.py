from collections import defaultdict

# Define a function to calculate sessions
def calculate_sessions(event_data):
    sessions_by_user = defaultdict(list)

    for event in event_data:
        visitor_id = event["visitorId"]
        timestamp = event["timestamp"]
        url = event["url"]

        if visitor_id not in sessions_by_user:
            current_session = {
                "duration": 0,
                "pages": [],
                "startTime": timestamp
            }
        else:
            current_session = sessions_by_user[visitor_id][-1]

        if (
            not current_session["pages"]
            or timestamp - current_session["startTime"] <= 600000
        ):
            current_session["duration"] = (
                timestamp - current_session["startTime"]
            )
            current_session["pages"].append(url)
        else:
            current_session = {
                "duration": 0,
                "pages": [url],
                "startTime": timestamp
            }
            sessions_by_user[visitor_id].append(current_session)

    return {"sessionsByUser": dict(sessions_by_user)}
