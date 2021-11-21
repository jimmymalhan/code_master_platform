# Single Cycle Check - Given a directed graph, check whether it contains a cycle or not.

# You're giveen an array of integers where each integer represents a jump of of its value in the array. For instance, 2 represents a jump of two indices forward in the array, the integer -3 represents a jump of three indices backward in the array.

# If a jump spills past the array's bounds, it wraps over to the other side. For instance, a jump of -1 at index 0 brings us to the last index in the array. Similarly, a jump of 1 at the last index in the array brings us to index 0.

# Write a function that returns a boolean representing whether the jumps in the array form a single cycle. A single cycle occurs if, starting at any index in the array and following the jumps, every element in the array is visited exactly once before landing back on the starting index.


# Concept:
# initialize - numElementsVisited , currentIdx =0, 0
# Condition - element at index 0 cannot be jumped through more than once and 
#   clause - (n+1)th element jump must be the first element you visited i.e index 0
#   increment the number of elements visited
#   currentIdx = # getNextIndex of the current element using (helper function)
# return if we have visited all elements and we are back at index 0
# create helper function
#   jump = visit the array at currentIdx
#   nextIdx = currentIdx + jump % len(array) #make sure you don't go out of bounds
#   return nextIdx is equal or greater than 0 else add the nextidx to the length of the array

class graph:
    def __init__(self, array):
        self.array = array

# O(n) time | O(1) space - where n is the length of the input array    

    def hasSingleCycle(self):
        numElementsVisited, currentIdx = 0, 0

        while numElementsVisited < len(self.array): # condition1
            if numElementsVisited > 0 and currentIdx == 0: # condition2
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