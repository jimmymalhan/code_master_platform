# Problem Name: Smallest Difference

# Problem Description:
# Write a function that takes in two non-empty arrays of integers, finds the pair of numbers (one from each array) whose absolute difference is closest to zero, and returns an array containing these two numbers, with the number from the first array in the first position.

# Note that the absolute difference of two integers is the distance between them on the real number line. For example, the absolute difference of -5 and 5 is 10, and the absolute difference of -5 and -4 is 1.

# You can assume that there will only be one pair of numbers with the smallest difference.

####################################
# Sample Input:
# arrayOne = [-1, 5, 10, 20, 28, 3]
# arrayTwo = [26, 134, 135, 15, 17]

# Sample Output:
# [28, 26]
####################################
"""
Explain the solution:
# Instead of generating all possible pairs of numbers, try somehow only looking at pairs that you know could actually have the smallest difference. How can you accomplish this?

# Would it help if the two arrays were sorted? If the arrays were sorted and you were looking at a given pair of numbers, could you efficiently find the next pair of numbers to look at? What are the runtime implications of sorting the arrays?

# Start by sorting both arrays, as per Hint #2. Put a pointer at the begining of both arrays and evaluate the absolute difference of the pointer-numbers. If the difference is equal to zero, then you've found the closest pair; otherwise, increment the pointer of the smaller of the two numbers to find a potentially better pair. Continue until you get a pair with a difference of zero or until one of the pointers get out of range of its array.

# O(nlog(n) + mlog(m)) time | O(1) space - where n is the length of the first input array and m is the length of the second input array

##################
Detailed explanation of the Solution:
function smallestDifference(arrayOne, arrayTwo):
    sort(arrayOne), sort(arrayTwo) in place
    intialize idxOne and idxTwo to 0
    intialize smallest and current to float("inf") #smallest is the smallest difference between two numbers and current is the current difference between two numbers
    intialize smallestPair to empty array
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo): # while both pointers are still in range of their arrays
        initialize firstNum and secondNum to the values of the array at the current index
        if firstNum < secondNum:
            current = secondNum - firstNum
            increment idxOne
        elif secondNum < firstNum:
            current = firstNum - secondNum
            increment idxTwo
        else: # if the numbers are equal, return the pair
            return [firstNum, secondNum] # if the numbers are equal, return the pair
        if smallest is greater that current:
            intialize smallest to current # update smallest to current
            initialize smallestPair is equal to [firstNum, secondNum]
    return smallestPair

"""
####################################

# O(nlog(n) + mlog(m)) time | O(1) space - where n is the length of the first input array and m is the length of the second input array.
# nlog(n) is the time to sort the first array and mlog(m) is the time to sort the second array.
# O(1) space is used because sorting is done in place.
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort(), arrayTwo.sort()
    idxOne, idxTwo = 0, 0
    smallest, current = float("inf"), float("inf") # keep track of the smallest difference and the current difference
    smallestPair = []
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo): # while both pointers are still in range of their arrays begining at the beginning of the arrays
        firstNum, secondNum = arrayOne[idxOne], arrayTwo[idxTwo]
        if firstNum < secondNum:
            current = secondNum - firstNum # update current to the difference between the two numbers
            idxOne += 1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            idxTwo += 1
        else:
            return [firstNum, secondNum] # if the numbers are equal, return the pair
        if smallest > current:
            smallest = current # update smallest to current
            smallestPair = [firstNum, secondNum]
    return smallestPair

print(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))