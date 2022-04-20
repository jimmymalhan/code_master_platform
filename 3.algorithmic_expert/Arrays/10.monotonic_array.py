# Problem Name: Monotonic Array

# Problem Description:
# Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic.

# An array is said to be monotonic if its elements, from left to right, are entirely non-increasing or entirely non-decreasing.

# Non-increasinf elements aren't necessarily exclusively decresing; they simply don't increase. Similarly, non-decreasing elements aren't necessarily exclusively increasing, they simply don't decrease.

# Note that empty arrays and arrays of one element are monotonic.

####################################
# Sample Input:
# [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]

# Sample Output:
# True
####################################
"""
Explain the solution:
- You can solve this question by iterating through the input array from left to right once.

- Try iterating through the input array from left to right, in search of two adjacent integers that can indicate whether the array is trending upward or downward. Once you've found the tentative trend of the array, at each element thereafter, compare the element of the previous one; if this comparison breaks the previously indentified trend, the arrau isn't monotonic.

- Alternatively, you can start by assuming that thr array is both entirely non-decresing and entirely non-increasing. As you iterate through each element, perform check to see if you can invalidare one or both of your assumptions.

# O(n) time | O(1) space - where n is the length of the array.


##################
Detailed explanation of the Solution:

"""
####################################

def isMonotonic(array):
    if len(array) <= 2:
        return True

    direction = array[1] - array[0]
    for i in range(2, len(array)):
        if direction == 0:
            direction = array[i] - array[i - 1]
            continue
        if breaksDirection(direction, array[i -1], array[i]):
            return False
    return True

def breaksDirection(direction, previousInt, currentInt):
    difference = currentInt - previousInt
    if direction > 0:
        return difference < 0
    return difference > 0

print(isMonotonic([-1, -5, -10, -1100, -1100, -1101, -1102, -9001]))