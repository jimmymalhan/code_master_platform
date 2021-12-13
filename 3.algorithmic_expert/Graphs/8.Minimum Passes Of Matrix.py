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

- 2. Once a positive value has been found and you can change its neighbors to positives, this positive value can no longer lead to the conversion of any negative values. Instead, its neighbors(that you just changed to positives) have the possibility of changing their own neighbors to positives. After you change a negatuve value to positive, you should store its position so that you can check if it can flip any of its neighbors in the next next pass of the matrix using BFS.

- 2 queue process:
- implementing a BFS, starting from all the positive-value positions in the array. Initialize a queue that stores the positions of all the positive values, iterate through the queue, dequeue elements out, and consider all of their neighbors. If any of their neighbors are negative, change them to positive, and store their positions in a secondary queue. Once the first queue is empty, Increment your number of passes, and iterate through the second queue you created(the one with the positions of negatives that were changed to positive). Repeat this process until no values are converted during a pass.

- 1 queue process:
- Differentiate the values that were already positive when the current pass started from the values that were changed to positive during the current pass.

# O(w * h) time | O(w * h) space where - w is the width of the matrix and h is the height of the matrix

##################
Detailed explanation of the Solution:

"""
####################################

def minimumPassesOfMatrix(matrix):
    pass

def main():
    matrix = [
        [0, -1, -3, 2, 0],
        [1, -2, 5, -1, -3],
        [3, 0, 0, -4, -1],
    ]
    print(minimumPassesOfMatrix(matrix)) # 3

if __name__ == "__main__":
    main()