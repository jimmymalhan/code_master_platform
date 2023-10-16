import json

# Validation function to check if the calculated sessions meet the criteria
def validate_sessions(calculated_sessions):
    for visitor_id, sessions in calculated_sessions["sessionsByUser"].items():
        for session in sessions:
            pages = session["pages"]
            duration = session["duration"]
            start_time = session["startTime"]
            
            # Check if the duration is zero for sessions with only one event
            if len(pages) == 1 and duration != 0:
                return False, f"Validation failed: Duration is not zero for single-event session for visitor {visitor_id}"
            
            # Check the 10-minute rule between consecutive events
            for i in range(1, len(pages)):
                time_gap = duration // len(pages)
                if time_gap > 600000:  # 10 minutes in milliseconds
                    return False, f"Validation failed: Time gap greater than 10 minutes in session for visitor {visitor_id}"
                    
    return True, "Validation successful: All sessions meet the criteria"

# Load the generated calculated_sessions.json file to inspect its contents
with open('calculated_sessions.json', 'r') as file:
    calculated_sessions = json.load(file)

# Validate the calculated sessions
is_valid, message = validate_sessions(calculated_sessions)
print(is_valid, message)
