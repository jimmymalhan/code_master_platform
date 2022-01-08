# Problem Name: Single Cycle Check 

# Problem Description:
# Given a directed graph, check whether it contains a cycle or not.

# You're given an array of integers where each integer represents a jump of of its value in the array. For instance, 2 represents a jump of two indices forward in the array, the integer -3 represents a jump of three indices backward in the array.

# If a jump spills past the array's bounds, it wraps over to the other side. For instance, a jump of -1 at index 0 brings us to the last index in the array. Similarly, a jump of 1 at the last index in the array brings us to index 0.

# Write a function that returns a boolean representing whether the jumps in the array form a single cycle. A single cycle occurs if, starting at any index in the array and following the jumps, every element in the array is visited exactly once before landing back on the starting index.

####################################
# Sample Input:
# array = [2, 3, 1, -4, -4, 2]

# Sample Output:
# True
####################################
"""
Explain the Solution:
1. Keep track of counter as you jump through the elements.
2. If you start at index 0 and jump through n elements, meet the following conditions:
    a. Starting element at index 0 cannot be jumped through more than once
    b. (n+1) element must be the first element you visited
# O(n) time | O(1) space - where n is the length of the input array

##################
Detailed explanation of the Solution:
function hasSingleCycle(array)
    initialize - numElementsVisited , currentIdx = 0, 0
    while numElementsVisited is less than length of an array: #Condition - element at index 0 cannot be jumped through more than once
        if numElementsVisited is greater than 0 and currentIdx is equilized to 0 # clause - (n+1)th element jump must be the first element you visited i.e index 0
            return False
        increment the numElementsVisited
        intialize currentIdx = getNextIndex of the currentIdx, array using (helper function)
    return currentIdx is equilized to 0 # if we have visited all elements and we are back at index 0

function getNextIndex(currentIdx, array):
  initialize jump to be equal to the array at currentIdx # value of the current element
  nextIdx is equal to (currentIdx + jump) % len(array) # make sure you don't go out of bounds
  return nextIdx if nextIdx is greater than and equal to 0 else nextIdx + length of the array
"""
####################################

class graph:
    def __init__(self, array: list):
        self.array = array

# O(n) time | O(1) space - where n is the length of the input array    

    def hasSingleCycle(self):
        numElementsVisited, currentIdx = 0, 0

        while numElementsVisited < len(self.array): # condition a.
            if numElementsVisited > 0 and currentIdx == 0: # condition b.
                return False # if we have visited more than 1 element and we are back at index 0
            numElementsVisited += 1 # increment the number of elements visited
            currentIdx = self.getNextIndex(currentIdx, self.array) # get next index of the current element
        return currentIdx == 0 # if we have visited all elements and we are back at index 0
    
    def getNextIndex(self, currentIdx, array):
        jump = self.array[currentIdx] # print(jump) # [2, 1, -4, 2, 3, -4] # visit the array at current index
        nextIdx = (currentIdx + jump) % len(self.array) # len(self.array) - to make sure we don't go out of bounds
        # print(nextIdx) # [2, 3, 5, 1, 4, 0]
        return nextIdx if nextIdx >= 0 else nextIdx + len(self.array) # if nextIdx is equal or greater than 0 else add the nextidx to the length of the array

def main():
    givenArray1 = graph([2, 3, 1, -4, -4, 2])
    print(givenArray1.hasSingleCycle())

    givenArray2 = graph([2, 2, -1])
    print(givenArray2.hasSingleCycle())

if __name__ == '__main__':
    main()