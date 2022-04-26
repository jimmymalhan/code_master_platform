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
create function called isMonotonic that takes in an arrays:
    initialize a variable called isNonDecreasing equal to True
    initialize a variable called isNonIncreasing equal to True
    iterate through the array from left to right once starting at index 1:
        if the current element is less than the previous element:
            set isNonDecreasing to False
        if the current element is greater than the previous element:
            set isNonIncreasing to False

    return isNonDecreasing or isNonIncreasing # if the array is entirely non-decreasing or entirely non-increasing, return True
"""
####################################

# Solution1 checks if the array is either non-increasing or non-decreasing.

def isMonotonic(array):
    if len(array) <= 2: # If the array is empty or has only one element, it is monotonic.
        return True

    direction = array[1] - array[0] # direction is a way to establish the trend of the array (increasing or decreasing).
    for i in range(2, len(array)):
        if direction == 0: # If the array is equalized entirely non-increasing or non-decreasing
            direction = array[i] - array[i - 1] # updating direction by subtracting the current element from the previous one.
            continue
        if breaksDirection(direction, array[i -1], array[i]):
            return False
    return True

def breaksDirection(direction, previousInt, currentInt):
    difference = currentInt - previousInt # difference between the current and previous integers.
    if direction > 0: # If the array is non-decreasing
        return difference < 0 # If the difference is negative, the array is not monotonic.
    return difference > 0 # If the difference is positive, the array is not monotonic.

print(isMonotonic([-1, -5, -10, -1100, -1100, -1101, -1102, -9001]))


# Solution1 checks if the array is non-increasing ONLY

def isMonotonic2(array):
    isNonDecreasing = True
    isNonIncreasing = True

    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            isNonDecreasing = False
        if array[i] > array[i - 1]:
            isNonIncreasing = False
    return isNonDecreasing or isNonIncreasing # If the array is equalized entirely non-increasing or non-decreasing


print(isMonotonic2([-1, -5, -10, -1100, -1100, -1101, -1102, -9001]))