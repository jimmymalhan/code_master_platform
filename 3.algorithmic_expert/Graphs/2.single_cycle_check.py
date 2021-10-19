# element at index 0 cannot be jumped through more than once and 
# (n+1)th element jump must be the first element you visited i.e index 0

# O(n) time | O(1) space - where n is the length of the input array


class graph:
    def __init__(self, array):
        self.array = array
    
    def hasSingleCycle(self):
        numElementsVisited = 0
        currentIdx = 0

        while numElementsVisited < len(self.array):
            if numElementsVisited > 0 and currentIdx == 0:
                return False
            numElementsVisited += 1
            currentIdx = self.getNextIndex(currentIdx, self.array)
        return currentIdx == 0
    
    def getNextIndex(self, currentIdx, array):
        jump = self.array[currentIdx]
        # print(jump) # [2, 1, -4, 2, 3, -4]
        nextIdx = (currentIdx + jump) % len(self.array)
        # print(nextIdx) # [2, 3, 5, 1, 4, 0]
        return nextIdx if nextIdx >= 0 else nextIdx + len(self.array)

def main():
    givenArray1 = graph([2, 3, 1, -4, -4, 2])
    print(givenArray1.hasSingleCycle())

    givenArray2 = graph([2, 2, -1])
    print(givenArray2.hasSingleCycle())

if __name__ == '__main__':
    main()