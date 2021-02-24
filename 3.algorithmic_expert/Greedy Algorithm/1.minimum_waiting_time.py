# O(nlogn) time -> (because of sorting)| O(1) space
# queries will always be 1 ?
def minimumWaitingTime(queries):
	queries.sort()
	totalWaitingTime = 0
	
	for idx, duration in enumerate(queries):
		queriesLeft = len(queries) - (idx + 1) # increment the idx to keep track of queries left
		totalWaitingTime += duration * queriesLeft
	
	return totalWaitingTime