# https://www.algoexpert.io/questions/Remove%20Islands

# You're given a two-dimensional array(a matrix) of potentionally unequal height and width containing only 0s and 1s. The matrix represents a two-toned image, where each 1 represents black and each 0 represents white. An island is a defined as any number of 1s that are horizontally or vertically adjacent(not diagonally adjacent) and that don't touch the border of the image. In other words, a group of horizontally or vertically adjacent 1s isin't an island is any of those 1s are in the first row, last row, first column, or last column of the input matrix.

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
# Explanation on the question:
# Remove islands = remove all the 1s that are not connected to the border horizontally or vertically (not diagonally)

# Hints:
# Find the positions of all the non-island 1s and store. Use dfs on all the 1st that are on the border of the image. Afterwards, you can easily identify and remove all the islands 1s from the input matrix by relying on the DS that you used to store the positions of the non-island 1s.

# You can also solve this problem without the use of a DS that stores the positions of the non-island 1s. Simply loop through the border of the image, and perform DFS on all positions with the value 1. Find all the 1s that are connected to the original position on the border, and change them from 1 to 2. After changing all non-island 1s to 2s, you can simply remove all the remaining 1s which are guranteed to be islands, from the matrix(by replacing them with 0s), and you can then change all the 2s back to 1s, since these were previously determined to be non-islands.

####################################
# A) Brute Force approach:
####################################
# loop the matrix and check if the current position is 1. If it is, then check if it is on the border of the matrix then perform DFS on the current position.
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

class Solution:
    def removeIslands(self, matrix):
        return []
