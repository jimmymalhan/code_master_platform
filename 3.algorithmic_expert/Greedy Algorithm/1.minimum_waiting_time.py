# (nlogn) time | O(1) space
def minimumWaitingTime(queries):
    queries.sort()
	
	totalWaitingTime = 0
	for idx, duration in enumerate(queries):
		queriesLeft = len(queries) - (idx + 1)
		totalWaitingTime += duration * queriesLeft
		
    return totalWaitingTime