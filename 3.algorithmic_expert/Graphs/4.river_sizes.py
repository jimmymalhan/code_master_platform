# https://www.algoexpert.io/questions/River%20Sizes

# You are given a two-dimensional array (matrix) of potentially unequal height and width containing only 0s and 1s. Each 0 represents land, and each 1 represents part of a river. A river consists of any number of 1s that are either horizontally or vertically adjacent (but not diagonally adjacent). The number of adjacent 1s forming a river determine its size. Write a function that returns an array of the sizes of all rivers represented in the input matrix. Note that these sizes do not need to be in any particular order. 

# Sample input:
# matrix = [
#     [1, 0, 0, 1, 0],
#     [1, 0, 1, 0, 0],
#     [0, 0, 1, 0, 1],
#     [1, 0, 1, 0, 1],
#     [1, 0, 1, 1, 0],
# ]

# Sample output:
# [1, 2, 2, 2, 5]

## The rivers can be clearly seen below.
# [
#     [1, , , 1,  ],
#     [1, ,1,  ,  ],
#     [ , ,1,  , 1],
#     [1, ,1,  , 1],
#     [1, ,1, 1,  ],
# ]

# Solution explanation:
# 1: 1 # there is only one 1
# 2: 2 # there are two 1s in a row
# 3: 2 # there are two 1s in a row
# 4: 2 # there are two 1s in a row
# 5: 5 # there are five 1s in a L shaped row

"""
stacks = breadth first search
queue = depth first search
"""
# Explain the solution:

# 1. Return the sizes of the rivers horizontally and vertically adjacent 1s in as traversing the matrix. Treat matrix as a graph where each element is a node with upto 4 neighbors nodes(left, right, top, bottom) and traverse the graph using DFS.
# 2. While traversing the matrix, anytime you encounter a 1, taverse entire river that this 1 is part of(keep track of the size of the river) by node's neighboring nodes and their own neighboring nodes as long as they are 1s. if you encounter a 0, mark it as visited and continue.
# 3. In order to prevent mistakenly calculating the size of the river multiple times, use auxiliary data structure "queue" to perform computation on unvisited nodes only. 


# Solution 1:
def riverSizes(matrix):
    sizes = [] # holds the sizes of the rivers
    visited = [[False for value in row] for row in matrix] # intially, intialzing the visited matrix to False # holds the visited nodes # output: [1, 2, 2, 2, 5] 

    # iterate through the matrix row by row and check if the element is 1 # if it is 1, add it to the queue # if it is 0, add it to the queue
    for i in range(len(matrix)): # iterate through the rows
        for j in range(len(matrix[i])): # iterate through the rows
            if visited[i][j]: # if the node has been visited, continue or if visited[i][j] == True
                continue
            traverseNode(i, j, matrix, visited, sizes) # if the node has not been visited, traverse the node
    return sizes

def traverseNode(i, j, matrix, visited, sizes): # i is the row, j is the row
    currentRiverSize = 0 # holds the size of the river
    # depth first search # stack
    nodesToExplore = [[i, j]] # holds the nodes to explore # stack
    while len(nodesToExplore): # while there are nodes to explore
        currentNode = nodesToExplore.pop() # pop the last node from the queue
        i = currentNode[0] # get the row
        j = currentNode[1] # get the row
        if visited[i][j]: # if the node has been visited, continue
            continue
        visited[i][j] = True # mark the node as visited
        if matrix[i][j] == 0: # if the node is 0, add it to the queue
            continue
        currentRiverSize += 1 # increment the river size # if the node is 1, add it to the queue
        unvisitedNeighbors = getUnvisitedNeighbors(i, j, matrix, visited) # get the unvisited neighbors of the node
        for neighbor in unvisitedNeighbors: # iterate through the unvisited neighbors
            nodesToExplore.append(neighbor) # add the neighbor to the queue
    if currentRiverSize > 0: # if the river size is greater than 0
        sizes.append(currentRiverSize) # add the river size to the sizes array

def getUnvisitedNeighbors(i, j, matrix, visited):
    unvisitedNeighbors = [] # holds the unvisited neighbors
    if i > 0 and not visited[i - 1][j]: # if the row is greater than 0 and the node has not been visited ABOVE the node
        unvisitedNeighbors.append([i - 1, j]) # add the node to the unvisited neighbors
    if i < len(matrix) - 1 and not visited[i + 1][j]: # if the row is less than the length of the matrix and the node has not been visited BELOW the node
        unvisitedNeighbors.append([i + 1, j]) # add the node to the unvisited neighbors
    if j > 0 and not visited[i][j - 1]: # if the row is greater than 0 and the node has not been visited to the LEFT of the node
        unvisitedNeighbors.append([i, j - 1]) # add the node to the unvisited neighbors 
    if j < len(matrix[0]) - 1 and not visited[i][j + 1]:# if the row is less than the length of the matrix and the node has not been visited to the RIGHT of the node
        unvisitedNeighbors.append([i, j + 1]) # add the node to the unvisited neighbors
    return unvisitedNeighbors

def main():
    matrix = [
        [1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0],
    ]
    print(riverSizes(matrix))

if __name__ == '__main__':
    main()