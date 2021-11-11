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

# The islands that were removed can be clearlt seen here:
#   [
#     [ ,  ,  ,  ,  ,  ],
#     [ , 1,  ,  ,  ,  ],
#     [ ,  , 1,  ,  ,  ],
#     [ ,  ,  ,  ,  ,  ],
#     [ ,  , 1, 1,  ,  ],
#     [ ,  ,  ,  ,  ,  ],
# ]

# Hints:


# Explanation of the solution:
#   We start by iterating through the matrix and marking all the 1s that are not touching the border of the matrix.
#   Then, we iterate through the matrix again and replace all the 1s that are touching the border with 0s.

