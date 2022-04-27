# Problem Name: Spiral Traverse

# Problem Description:
# Write a function that takes an n x m two-dimendional array (that can be square-shaped when n == m) and returns a one-dimensional array of all array's elements in spiral order.

# Spiral order starts at the top left corner of the two-dimensional array, goes to the right, and proceeds in a spiral pattern all the way until every element has been visited.

####################################
# Sample Input:
array =  [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
  ]
# Sample Output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

####################################
"""
Explain the solution:

##################
Detailed explanation of the Solution:
1- You can think of the spiral that you have to traverse as a set of rectangle perimeters that progressively get smaller and smaller(i.e that progressively move inwards in the two-dimensional array).

2- Going off of Hint #1, declare four variables: a starting row, a starting column, an ending row, and an ending column. These four variables represent the bounds of the first rectangle perimeter in the spiral that you have to traverse. Traverse that perimeter using those bounds, and then move the bounds inwards. End your algorith once the starting row passes the ending row or the starting column passes the ending column.

3- You can solve this problem both iteratively and recursively following very similar logic.

# O(n) time | O(n) space - where n is the total number of elements in the array,
"""
####################################

def spiralTraverse(array):
    # Write your code here.
    result = []
    startRow = 0
    startCol = 0
    endRow = len(array) - 1
    endCol = len(array[0]) - 1
    while startRow <= endRow and startCol <= endCol:
        # Traverse top row
        for i in range(startCol, endCol + 1):
            result.append(array[startRow][i])
        startRow += 1
        # Traverse right column
        for i in range(startRow, endRow + 1):
            result.append(array[i][endCol])
        endCol -= 1
        # Traverse bottom row
        if startRow <= endRow:
            for i in range(endCol, startCol - 1, -1):
                result.append(array[endRow][i])
            endRow -= 1
        # Traverse left column
        if startCol <= endCol:
            for i in range(endRow, startRow - 1, -1):
                result.append(array[i][startCol])
            startCol += 1
    return result

print(spiralTraverse([
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
  ]))