# Problem Name: Move Element To End

# Problem Description:
# You're given an array of integets and an integer. Write a function that moves all instances of that integer in the array to the end of the array and returns the array.

# The function should perform this in place (i.e., it should mutate the input array) and doesn't need to maintain the order of the other elements.

####################################
# Sample Input:
# array = [2, 1, 2, 2, 2, 3, 4, 2]
# toMove = 2

# Sample Output:
# [1, 3, 4, 2, 3, 2, 2, 2] # the numbers 1, 3, and 4 could be in any order
####################################
"""
Explain the solution:

1. You can solve this problem in linear time.

2. In view of Hint #1, you can solve this problem without sorting the input array. Try setting two pointers at the start and end of the array, respectively, and progressively moving them inwards until they meet.

3. Following Hint #2, set two pointers at the start and end of the array, respectively. Move the right pointer inward so long as it points to the integer to move, and move the left pointer inwards so long as it doesn't point to the integer to move. When both pointers aren't moving, swap their values in place. Repeat this process until the pointers pass each other.

# O(n) time | O(1) space - where n is the length of the input array

##################
Detailed explanation of the Solution:
function moveElementToEnd(array, toMove):
    initialize left and right pointers at the start and end of the array respectively
    while left less than right:
        if array[left] is not equal to toMove:
            increment left
        elif array[right] is equal to toMove:
            decrement right
        else: # array[left] is equal to toMove and array[right] is not equal to toMove
            swap array[left] and array[right]
            increment left
            decrement right
    return array
"""
####################################

def moveElementToEnd(array, toMove):
    left = 0
    right = len(array) - 1
    while left < right:
        if array[left] != toMove:
            left += 1
        elif array[right] == toMove:
            right -= 1
        else: # array[left] == toMove and array[right] != toMove
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    return array

print(moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2))