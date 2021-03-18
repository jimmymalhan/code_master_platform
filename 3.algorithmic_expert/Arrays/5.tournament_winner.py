# brute force approach
	# create a DS - hash map
	# loop through the competitions
    # seperate home and away team 
    # define winning team -
        # if the competition's element is winner based on the results
    # update scores by 3 points
    # find the best team in the scores

# optimization - create a new variable to track the winner element
	# compare the current element's score with the winner element (in new variable) until finished

# O(n) time | O(k) space
# n - number of competitions or length of results (iteration)
# k - number of teams in the competitions (to store in DS - hash map)

Home_Team_Won = 1 # constant variable to make code the code more readable
def tournamentWinner(competitions, results):
	currentBestTeam = ""
	scores = {currentBestTeam: 0} # defined hashMap DS
	
	for idx, competition in enumerate(competitions):
		result = results[idx]
        #print(results)
            # [0, 0, 1]
            # [0, 0, 1]
            # [0, 0, 1]
        # print(results[idx])
            # 0
            # 0
            # 1

		homeTeam, awayTeam = competition # splitting the array for homeTeam and awayTeam
		# defining the winningTeam by checking the result is equal to Home_Team_Won
		winningTeam = homeTeam if result == Home_Team_Won else awayTeam 
		# updating the winningTeam's scores in the DS
		updateScores(winningTeam, 3, scores)
		# update the current best team
		if scores[winningTeam] > scores[currentBestTeam]:
			currentBestTeam = winningTeam
	return currentBestTeam

def updateScores(team, points, scores):
	if team not in scores: # if the scores are not defined for the team
		scores[team] = 0 # assigning that team's value to be zero
	
	scores[team] += points # else - updating the team's points (by 3 as defined)