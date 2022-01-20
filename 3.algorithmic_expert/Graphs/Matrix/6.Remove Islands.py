# Problem Name: Remove Islands

# Problem Description:
# You're given a two-dimensional array(a matrix) of potentially unequal height and width containing only 0s and 1s. The matrix represents a two-toned image, where each 1 represents black and each 0 represents white. An island is a defined as any number of 1s that are horizontally or vertically adjacent(not diagonally adjacent) and that don't touch the border of the image. In other words, a group of horizontally or vertically adjacent 1s isin't an island is any of those 1s are in the first row, last row, first column, or last column of the input matrix.

# Note that an island can twist. In other words, it doesn't have to be straight vertical line or straight horizontal line; it can L-shaped, for example.
# You can think of islands as patches of black that don't touch the border of the two-toned image.
# Write a function that returns a modified version of the input matrix, where all the islands are removed. You remove an island by replacing it with 0s.
# Naturally, you're allowed to change the input matrix.

####################################
# Sample Input:
# matrix = [
#     [1, 0, 0, 0, 0, 0],
#     [0, 1, 0, 1, 1, 1],
#     [0, 0, 1, 0, 1, 0],
#     [1, 1, 0, 0, 1, 0],
#     [1, 0, 1, 1, 0, 0],
#     [1, 0, 0, 0, 0, 1],
# ]

# Sample Output:
#   [
#     [1, 0, 0, 0, 0, 0],
#     [0, 0, 0, 1, 1, 1],
#     [0, 0, 0, 0, 1, 0],
#     [1, 1, 0, 0, 1, 0],
#     [1, 0, 0, 0, 0, 0],
#     [1, 0, 0, 0, 0, 1],
# ]

# The islands that were removed can be clearly seen here:
#   [
#     [ ,  ,  ,  ,  ,  ],
#     [ , 1,  ,  ,  ,  ],
#     [ ,  , 1,  ,  ,  ],
#     [ ,  ,  ,  ,  ,  ],
#     [ ,  , 1, 1,  ,  ],
#     [ ,  ,  ,  ,  ,  ],
# ]

# -  Remove islands = remove all the 1s that are not connected to the border horizontally or vertically (not diagonally)
# - If it is connected to the border, that is not an island.

####################################
# A) Brute Force approach: O(n^2) time complexity and O(n) space complexity
####################################
# loop the matrix and check the current position -
    # if it is on the border of the matrix then perform DFS on the current position.
    # if the current position is 1, then check if it is not a neighbor of the border which is 1, then we can replace it with 0.

####################################
# B) Optimal Solution than brute force > reduce the time complexity to O(n), where n is the number of 1s in the matrix
####################################
# Build Auxilary Data Structure =>> Intialize False for all positions in the matrix.
    # 1. Loop through the EXTERIOR/BORDER of the image and find all of the 1s which are connected to the border and mark them as True (perform DFS on all the 1s).
        ## DFS:
            # Check Vertically and Horizontally if the position is 0, then we skip the position.
            # if the position is 1, then we mark the position as True, and perform DFS on the position horizontally and vertically if they are 1 as well (not diagonally) and mark them as True as well (so that we don't visit them again).

    # 2. Loop through INTERIOR/INNER positions(not on the border) and if the value is 1 and doesn't have the value True, then we replace it with 0. If the position is 1 and has the value True, then we skip the position.

# O(wh) time | O(wh) space(coz of identical DS) - where w and h are the width and height of the matrix
def removeIslands(matrix):
    onesConnectedToBorder = [[False for col in matrix[0]] for row in matrix] # connected to the border

    # Find all the 1s that are not islands
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            rowIsBorder = row == 0 or row == len(matrix) - 1 # check if the row is on the border 
            colIsBorder = col == 0 or col == len(matrix[row]) - 1 # check if the col is on the border
            isBorder = rowIsBorder or colIsBorder # check if the position is on the border
            if not isBorder:
                continue

            if matrix[row][col] != 1:
                continue # skip the position if it's not a 1

            findOnesConnectedToBorder(matrix, row, col, onesConnectedToBorder) # perform DFS on all the 1s that are connected to the border

    for row in range(1, len(matrix) - 1):
        for col in range(1, len(matrix[row]) - 1):
            if onesConnectedToBorder[row][col]: # if the position is 1 and has the value True, then we skip the position
                continue
                
            matrix[row][col] = 0 # replace the position with 0
    return matrix

def findOnesConnectedToBorder(matrix, startRow, startCol, onesConnectedToBorder):
    stack = [(startRow, startCol)] # push the starting position into the stack
    
    while len(stack) > 0:
        currentPosition = stack.pop() # pop the last element from the stack
        currentRow, currentCol = currentPosition # unpack the current position # currentRow = currentPosition[0], currentCol = currentPosition[1]
        
        alreadyVisited = onesConnectedToBorder[currentRow][currentCol] # mark the current position as True
        if alreadyVisited:
            continue
        
        onesConnectedToBorder[currentRow][currentCol] = True # mark the current position as True
        
        neighbors = getNeighbors(matrix, currentRow, currentCol) # get all the neighbors of the current position
        for neighbor in neighbors:
            row, col = neighbor # unpack the neighbor # row = neighbor[0], col = neighbor[1]
            if matrix[row][col] != 1:
                continue # skip the neighbor if it is not a 1
            stack.append(neighbor) # push the neighbor into the stack

def getNeighbors(matrix, row, col):
    neighbors = []
    
    numRows = len(matrix)
    numCols = len(matrix[row])

    if row - 1 >= 0: # UP # check if the row is not on the border
        neighbors.append((row - 1, col)) # push the neighbor into the neighbors list
    if row + 1 < numRows: # DOWN # check if the row is not on the border
        neighbors.append((row + 1, col))
    if col - 1 >= 0: # LEFT # check if the col is not on the border
        neighbors.append((row, col - 1)) #
    if col + 1 < numCols: # RIGHT # check if the col is not on the border
        neighbors.append((row, col + 1))
    return neighbors

####################################
# C) Optimal Solution: Better Average space complexity
####################################
"""
Explain the Solution:
Note: Don't need to create Auxilary DS
    1. Loop through the EXTERIOR/BORDER of the image and find all of the 1s which are connected to the border and change them to 2.
        # DFS:
            Check Vertically and Horizontally if the position is 0, then we skip the position.
            If the position is 1, then we mark the position as 2, and perform DFS on the position horizontally and vertically if they are 1 as well (not diagonally) and mark them as 2 as well (so that we don't visit them again).
    2. Loop through the matrix, we simply change all the 2s back to 1s and change all the 1s to 0s.

O(wh) time | O(wh) space - where w and h are the width and height of the matrix

Its same space complexity as we need to perform DFS on the matrix using Stack. Suppose if we have all 1s in the matrix, then we need to perform DFS on all the 1s, so the space complexity is O(wh) and stack needs to store all the positions of the 1s.

    - It has better Average Space Complexity than the other two solutions

##################
Detailed explanation of the Solution:
function for removeIsIslands for matrix
    loop for row in range to len of matrix
        loop for col in range to len of matrix for row
            rowIsBorder is equal to row is equalized to 0 or row is equalized to len of matrix - 1 # to check if row is border
            colIsBorder is equal to col is equalized to 0 or col is equalized to len of matrix for row - 1 # to check if col is border
            isBorder is equal to rowIsBorder or colIsBorder # to check if row or col is border
            if not isBorder # if the position is not a border
                continue
            if matrix[row][col] is not equal to 1 # if the position is not a 1
                continue
            changeOnesConnectedToBorderToTwos for matix, row, col # change all 1s connected to border to 2s using DFS

    loop for row in range to len of matrix
        loop for col in range to len of matrix for row
            color is equal to matrix[row][col] # color of the current position
            if color is equalized to 1
                matrix[row][col] is equal to 0 # change color to 0
            if color is equalized to 2
                matrix for row,col is equal to 1 # change color to 1
    return matrix

function changeOnesConnectedToBorderToTwos for matrix, startRow, startCol
    stack is equal to [(startRow, startCol)] # stack to store the positions to be checked
    while len of stack is greater than 0
        currentPosition = stack.pop() # pop the last position from the stack
        currentRow, currentCol = currentPosition # get the row and col of the current position
        matrix for [currentRow][currentCol] is equal to 2 # mark the current position as 2
        neighbors is equal to getNeighbors for matrix, currentRow, currentCol # get the neighbors of the current position
        loop for neighbor in neighbors
            row, col = neighbor # get the row and col of the neighbor
            if matrix for [row][col] is not equal to 1
                continue # skip the neighbor if it is not a 1    
            append the neighbor to the stack

function getNeighbors for matrix, row, col
    neighbors is equal to [] # list to store the neighbors
    numRows is equal to len of matrix
    numCols is equal to len of matrix for row

    if row - 1 is greater than and equal to 0:
        neighbors.append((row - 1, col)) # add the neighbor to the list # `UP`
    if row + 1 is less than to numRows:
        neighbors.append((row + 1, col)) # add the neighbor to the list # `DOWN`
    if col - 1 is greater than and equal to 0:
        neighbors.append((row, col - 1)) # add the neighbor to the list # `LEFT`
    if col + 1 is less than to numCols:
        neighbors.append((row, col + 1)) # add the neighbor to the list # `RIGHT`
    return neighbors
"""

def removeIslandsOptimized(matrix):
    # Find all the 1s that are not islands
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            rowIsBorder = row == 0 or row == len(matrix) - 1 # check if the row is on the border 
            colIsBorder = col == 0 or col == len(matrix[row]) - 1 # check if the col is on the border
            isBorder = rowIsBorder or colIsBorder # check if the position is on the border
            if not isBorder: # if the position is not on the border
                continue

            if matrix[row][col] != 1:
                continue # skip the position if it's not a 1

            changeOnesConnectedToBorderToTwos(matrix, row, col) # change all ones connected to border to twos using DFS

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            color = matrix[row][col] # get the color of the position
            if color == 1: # if the position is 1, then we replace it with 0
                matrix[row][col] = 0 # replace the position with 0
            elif color == 2: # if the position is 2, then we replace it with 1
                matrix[row][col] = 1 # replace the position with 1
    return matrix

def changeOnesConnectedToBorderToTwos(matrix, startRow, startCol):
    stack = [(startRow, startCol)] # push the starting position into the stack
    
    while len(stack) > 0:
        currentPosition = stack.pop() # pop the last element from the stack
        currentRow, currentCol = currentPosition # unpack the current position # currentRow = currentPosition[0], currentCol = currentPosition[1]
        
        matrix[currentRow][currentCol] = 2 # mark the current position as 2

        neighbors = getNeighbors(matrix, currentRow, currentCol) # get all the neighbors of the current position

        for neighbor in neighbors:
            row, col = neighbor # unpack the neighbor # row = neighbor[0], col = neighbor[1]
            if matrix[row][col] != 1:
                continue # skip the neighbor if it is not a 1
            stack.append(neighbor) # add the neighbor into the stack

def getNeighbors(matrix, row, col):
    neighbors = []
    
    numRows = len(matrix)
    numCols = len(matrix[row])

    if row - 1 >= 0: # UP # check if the row is not on the border
        neighbors.append((row - 1, col)) # push the neighbor into the neighbors list
    if row + 1 < numRows: # DOWN # check if the row is not on the border
        neighbors.append((row + 1, col))
    if col - 1 >= 0: # LEFT # check if the col is not on the border
        neighbors.append((row, col - 1)) #
    if col + 1 < numCols: # RIGHT # check if the col is not on the border
        neighbors.append((row, col + 1))
    return neighbors

def main():
    matrix = [
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
        [1, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 1],
    ]
    # print(removeIslands(matrix))
    print(removeIslandsOptimized(matrix))

if __name__ == "__main__":
    main()