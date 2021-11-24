# https://www.algoexpert.io/questions/Remove%20Islands

# You're given a two-dimensional array(a matrix) of potentially unequal height and width containing only 0s and 1s. The matrix represents a two-toned image, where each 1 represents black and each 0 represents white. An island is a defined as any number of 1s that are horizontally or vertically adjacent(not diagonally adjacent) and that don't touch the border of the image. In other words, a group of horizontally or vertically adjacent 1s isin't an island is any of those 1s are in the first row, last row, first column, or last column of the input matrix.

# Note that an island can twist. In other words, it doesn't have to be straight vertical line or straight horizontal line; it can L-shaped, for example.
# You can think of islands as patches of black that don't touch the border of the two-toned image.
# Write a function that returns a modified version of the input matrix, where all the islands are removed. You remove an island by replacing it with 0s.
# Naturally, you're allowed to change the input matrix.

# Sample input:
# matrix = [
#     [1, 0, 0, 0, 0, 0],
#     [0, 1, 0, 1, 1, 1],
#     [0, 0, 1, 0, 1, 0],
#     [1, 1, 0, 0, 1, 0],
#     [1, 0, 1, 1, 0, 0],
#     [1, 0, 0, 0, 0, 1],
# ]

# Sample output:
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

"""
Remove islands = remove all the 1s that are not connected to the border horizontally or vertically (not diagonally)
- If it is connected to the border, that is not an island.
"""

# Hints:
# Find the positions of all the non-island 1s and store. Use dfs on all the 1st that are on the border of the image. Afterwards, you can easily identify and remove all the islands 1s from the input matrix by relying on the DS that you used to store the positions of the non-island 1s.

####################################
# A) Brute Force approach:
####################################
# loop the matrix and check if the current position -
# If it is on the border of the matrix then perform DFS on the current position.
# if the current position is 1, then check if it is not a neighbor of the border which is 1, then we can replace it with 0.
# O(n^2) time complexity and O(n) space complexity

####################################
# B) Optimal Solution than brute force > reduce the time complexity to O(n)
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
# Don't need to create Auxilary DS
# 1. Loop through the EXTERIOR/BORDER of the image and find all of the 1s which are connected to the border and change them to 2.
    ## DFS:
        # Check Vertically and Horizontally if the position is 0, then we skip the position.
        # if the position is 1, then we mark the position as 2, and perform DFS on the position horizontally and vertically if they are 1 as well (not diagonally) and mark them as 2 as well (so that we don't visit them again).
# 2. Loop through the matrix, we simply change all the 2s back to 1s and change all the 1s to 0s.

# O(wh) time | O(wh) space - where w and h are the width and height of the matrix

# Its same space complexity as we need to perform DFS on the matrix using Stack. Suppose if we have all 1s in the matrix, then we need to perform DFS on all the 1s, so the space complexity is O(wh) and stack needs to store all the positions of the 1s.

# Has better Average Space Complexity than the other two solutions



def main():
    matrix = [
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
        [1, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 1],
    ]
    print(removeIslands(matrix))
    # print(removeIslands2(matrix))

if __name__ == "__main__":
    main()