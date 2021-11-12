# https://www.algoexpert.io/questions/Remove%20Islands

# You're given a two-dimensional array(a matrix) of potentionally unequal height and width containing only 0s and 1s. The matrix represents a two-toned image, where each 1 represents black and each 0 represents white. An island is a defined  as any number of 1s that are horizontally or vertically adjacent(not diagonally adjacent) and that don't touch the border of the image. In other words, a group of horizontally or vertically adjacent 1s isin't an island is any of those 1s are in the first row, last row, first column, or last column of the input matrix.

# Note that an island can twist. In other words, it doesn't have to be straight vertical line or straight horizontal line; it can L-shaped, for example.

# You can think of islands as patches of black that don't touch the border of the two-toned image.

# Write a function that returns a modified version of the input matrix, where all the islands are removed. You remove an island by replacing it with 0s.

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
#1. Remove islands(edge borders)
#2. Remove islands = remove all the 1s that are not connected to the border horizontally or vertically (not diagonally)

# Hints:
# find the positions of all the non-island 1s and store. Use dfs on all the 1st that are on the border of the image. Afterwards, you can easily identify and remove all the islands 1s from the input matrix by relying on the DS that you used to store the positions of the non-island 1s.

# You can also solve this problem without the use of a DS that stores the positions of the non-island 1s. Simply loop through the border of the image, and perform DFS on all positions with the value 1. Find all the 1s that are connected to the original position on the border, and change them from 1 to 2. After changing all non-island 1s to 2s, you can simply remove all the remaining 1s which are guranteed to be islands, from the matrix(by replacing them with 0s), and you can then change all the 2s back to 1s, since these were previously determined to be non-islands.

# Explanation of the solution:
#   We start by iterating through the matrix and marking all the 1s that are not touching the border of the matrix.
#   Then, we iterate through the matrix again and replace all the 1s that are touching the border with 0s.

# O(wh) time | O(wh) space - where w and h are the width and height of the matrix

class solution:
    def removeIslands(self, matrix):
        return []