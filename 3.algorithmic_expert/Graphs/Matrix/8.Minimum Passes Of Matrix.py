# Problem Name: Minimum Passes Of Matrix

# Problem Description:
# Write a function that takes in an integer matrix of potentially unequal height and width and returns the minimum number of passes required to convert all negative integers in the matrix to positive integers.

# A negative integer in the matrix can only be converted to a positive integer if one or more of its adjacent elements is positive. An adjacent element is an element that is to the left, to the right, above, or below the current element in the matrix. Converting a negative to a positive simply involves multiplying it by -1.

# Note that the 0 value is neither positive nor negative, meaning that a 0 can't convert an adjacent negative to a positive.

# A single pass through the matrix involves converting integers that can be converted at a particular point in the time. For example, consider the following input matrix:

# [
#  [0, -2, -1],
#  [-5, 2, 0],
#  [-6, -2, 0],
# ]

# After a first pass, only 3 values can be converted to positives:
# [
# [0, 2, -1],
# [5, 2, 0],
# [-6, 2, 0],
# ]

# After a second pass, the remaining negative values can be converted to positives:
# [
# [0, 2, 1],
# [5, 2, 0],
# [6, 2, 0],
# ]

# Note that the input matrix will always contain at least one element. If the negative integers in the input matrix can't be converted to positive, regardless of how many passes are run, your function should return -1.

# Sample Input:
# matrix = [
#  [0, -1, -3, 2, 0],
#  [1, -2, 5, -1, -3],
#  [3, 0, 0, -4, -1],
# ]

# Sample Output:
# 3 (The minimum number of passes is 3)
####################################
"""
Explain the solution:
- 1. The brute force approach is to simply iterate through the entire matrix and change the negative neighbors to positive. But, it look at the same elements in matrix multiple times which is not optimal.

- 2. Once a negative value has been found and you can change its neighbors to positives, this positive value can no longer lead to the conversion of any negative values. Instead, its neighbors (that you just changed to positives) have the possibility of changing their own neighbors to positives. After you change a negative value to positive, you should store its position so that you can check if it can flip any of its neighbors in the next pass of the matrix using BFS.

    - TWO queue process:
    - Implementing a BFS, starting from all the positive-value positions in the array. Initialize a queue that stores the positions of all the positive values, iterate through the queue, dequeue elements out, and consider all of their neighbors. If any of their neighbors are negative, change them to positive, and store their positions in a secondary queue. Once the first queue is empty, Increment your number of passes, and iterate through the second queue you created(the one with the positions of negatives that were changed to positive). Repeat this process until no values are converted during a pass.

# O(w * h) time | O(w * h) space where - w is the width of the matrix and h is the height of the matrix

##################
Detailed explanation of the Solution:

create a function for minimumPassesOfMatrix for matrix:
    intialize a variable passes equal to convertNegatives for matrix
    return passes - 1 if not containsNegative for matrix # if there is no negative value in the matrix, return -1

create a function for convertNegatives for matrix:
    nextPassQueue equal to getAllPositivePositions for matrix
    passes equal to 0

    while length of nextPassQueue is greater than 0:
        currentPassQueue equal to nextPassQueue # set the current pass queue to the next pass queue
        nextPassQueue equal to [] # reset the next pass queue

        while length of currentPassQueue is greater than 0: # while there are still values in the current pass queue
            currentRow, currentCol equal to currentPassQueue.pop(0) # In Python, popping elements from the start of a list is an O(n) operation. # To make this an O(1) operation, we could use the `deque` object. # For our time complexity analysis, we'll assume this runs in O(1) time. # Also, for this particular solution, we could actually just turn this queue into a stack and replace `.pop(0)` with the constant-time `.pop()` operation.

            adjacentPositions equal to getAdjacentPositions for currentRow, currentCol, matrix # get the adjacent positions of the current position
            for position in adjacentPositions: # iterate through the adjacent positions
                row, col equal to position # get the row and col of the adjacent position

                value equal to matrix[row][col] # get the value of the adjacent position
                if value < 0:
                    matrix[row][col] equal to value * -1 # change the value of the adjacent position to -1
                    nextPassQueue.append(position) # add the adjacent position to the next pass queue
        passes += 1 # increment the number of passes
    return passes

create a function for getAllPositivePositions for matrix:
    positivePositions equal to []
    for row in range of length of matrix:
        for col in range of length of matrix[row]:
            value equal to matrix[row][col]
            if value > 0:
                positivePositions.append([row, col])
    return positivePositions

create a function for getAdjacentPositions for row, col, matrix:
    adjacentPositions equal to []
    if row > 0:
        adjacentPositions.append([row - 1, col]) # up
    if row < len(matrix) - 1:
        adjacentPositions.append([row + 1, col]) # down
    if col > 0:
        adjacentPositions.append([row, col - 1]) # left
    if col < len(matrix[row]) - 1:
        adjacentPositions.append([row, col + 1]) # right
    return adjacentPositions

create a function for containsNegative for matrix:
    for row in range of matrix:
        for value in row:
            if value < 0:
                return True
    return False
"""
####################################
# Two queue process
def minimumPassesOfMatrix_2_queue(matrix):
    passes = convertNegatives(matrix)
    return passes - 1 if not containsNegative(matrix) else - 1 # if there is no negative value in the matrix, return -1

def convertNegatives(matrix):
    nextPassQueue = getAllPositivePositions(matrix)
	
    passes = 0
    
    while len(nextPassQueue) > 0:        # while there are still positive values in the matrix
        currentPassQueue = nextPassQueue # set the current pass queue to the next pass queue
        nextPassQueue = []               # reset the next pass queue      
		
        while len(currentPassQueue) > 0: # while there are still values in the current pass queue
            currentRow, currentCol = currentPassQueue.pop(0)
            # In Python, popping elements from the start of a list is an O(n) operation.
            # To make this an O(1) operation, we could use the `deque` object.
            # For our time complexity analysis, we'll assume this runs in O(1) time.
            # Also, for this particular solution, we could actually just turn this queue into a stack and replace `.pop(0)` with the constant-time `.pop()` operation.
            
            adjacentPositions = getAdjacentPositions( currentRow, currentCol, matrix)
            for position in adjacentPositions:
                row, col = position # get the row and col of the adjacent position
                
                value = matrix[row][col]
                if value < 0:
                    matrix[row][col] *= -1
                    nextPassQueue.append([row, col])
					
        passes += 1
		
    return passes

def getAllPositivePositions(matrix):
	positivePositions = []

	for row in range(len(matrix)):
		for col in range(len(matrix[row])):
			value = matrix[row][col]
			if value > 0:
				positivePositions.append([row, col])
	return positivePositions

def getAdjacentPositions(row, col, matrix):
    adjacentPositions = []
    numRows = len(matrix)
    numCols = len(matrix[row])
	
    if row > 0:
    	adjacentPositions.append([row - 1, col]) # up
    if row < numRows:
    	adjacentPositions.append([row + 1, col]) # down
    if col > 0:
    	adjacentPositions.append([row, col - 1]) # left
    if col < len(matrix[row]):
    	adjacentPositions.append([row, col + 1]) # right

    return adjacentPositions

def containsNegative(matrix):
	for row in matrix:
		for value in row:
			if value < 0:
				return True
	return False

####################################
# One queue process
# 3- ONE queue process:
# - Differentiate the values that were already positive when the current pass started from the values that were changed to positive during the current pass.

#     Meaning -> which values are processing in the current pass and which values are processing in the next pass.

# O(w * h) time | O(w * h) space where - w is the width of the matrix and h is the height of the matrix
def minimumPassesOfMatrix_1_queue(matrix):
    passes = convertNegatives(matrix)
    return passes - 1 if not containsNegative(matrix) else -1

def convertNegatives(matrix):
    queue = getAllPositivePositions(matrix)
    
    passes = 0
    
    while len(queue) > 0:
        currentSize = len(queue)
        
        while currentSize > 0:
            # In Python, popping elements from the start of a list is an O(n)-time operation.
            # To make this an O(1) operation, we could use the `deque` object.
            # For our time complexity analysis, we'll assume this runs in O(1) time.
            # Also, for this particular solution, we could actually just turn this queue into a stack and replace `.pop(0)` with the constant-time `.pop()` operation.
            currentRow, currentCol = queue.pop(0)
            
            adjacentPositions = getAdjacentPositions( currentRow, currentCol, matrix)
            for position in adjacentPositions:
                row, col = position
                
                value = matrix[row][col]
                if value < 0:
                    matrix[row][col] *= -1
                    queue.append([row, col])
                
            currentSize -= 1

        passes += 1
        
    return passes

def getAllPositivePositions(matrix):
    positivePositions = []

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            value = matrix[row][col]
            if value > 0:
                positivePositions.append([row, col])
    return positivePositions

def getAdjacentPositions(row, col, matrix):
    adjacentPositions = []
    
    if row > 0:
        adjacentPositions.append([row - 1, col]) # up
    if row < len(matrix) - 1:
        adjacentPositions.append([row + 1, col]) # down
    if col > 0:
        adjacentPositions.append([row, col - 1]) # left
    if col < len(matrix[0]) - 1:
        adjacentPositions.append([row, col + 1]) # right
    
    return adjacentPositions

def containsNegative(matrix):
    for row in matrix:
        for value in row:
            if value < 0:
                return True
    return False

def main():
    matrix = [
        [0, -1, -3, 2, 0],
        [1, -2, 5, -1, -3],
        [3, 0, 0, -4, -1],
    ]
    print(minimumPassesOfMatrix_2_queue(matrix)) #3- TWO queue process
    # print(minimumPassesOfMatrix_1_queue(matrix)) #3- ONE queue process

if __name__ == "__main__":
    main()