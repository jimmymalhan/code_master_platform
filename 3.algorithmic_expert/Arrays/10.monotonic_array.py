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
create function called isMonotonic that takes in an array of integers:
    if len of array is less than or equal to 2, return True # if the array is empty or has only one element, it is monotonic.

    inititalize direction equal by subtracting second element's index from first element's index.
    iterate through the array from index 2 to the end of the array:
        if direction is equalized to 0: # if the array is entirely non-increasing or non-decreasing or equal.
            
            direction is equal to subtracting the current element from the previous one.
            continue # continue to the next iteration of the loop.
        if breaksDirection for direction, array[i-1], array[i]:
            return False # if the direction breaks, return False.
    return True # if the loop completes, return True.

function breaksDirection takes in a direction, previousInt, and currentInt:
    difference is equal to currentInt - previousInt # difference between the current and previous integers.
    if direction is greater than 0: # if the array is non-decreasing
        return difference is less than 0 # if the difference is negative, the array is not monotonic.
    return difference is greater than 0 # if the difference is positive, the array is not monotonic.

"""
####################################

def isMonotonic(array):
    if len(array) <= 2: # If the array is empty or has only one element, it is monotonic.
        return True

    direction = array[1] - array[0] # initialize direction to the trend of the array because we know that the first two elements are the only ones that can break the trend.
    for i in range(2, len(array)):
        if direction == 0: # If the array is entirely non-increasing or non-decreasing or equal
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