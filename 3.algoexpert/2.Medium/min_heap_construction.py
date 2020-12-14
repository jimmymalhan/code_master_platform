# firstParentIdx = (len(array) - 2) // 2
# childOneIdx = currentIdx * 2 + 1 
# childTwoIdx = currentIdx * 2 + 2 
# parentIdx = (currentIdx - 1) // 2 

class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

	# O(n) time | O(1) space
    def buildHeap(self, array):
		firstParentIdx = (len(array) - 2) // 2
		for currentIdx in reversed(range(firstParentIdx + 1)):
			self.siftDown(currentIdx, len(array) - 1, array)
		return array
	
	# O(log(n) time, O(1) space)
    def siftDown(self, currentIdx, endIdx, heap): # compare both childs
		childOneIdx = currentIdx * 2 + 1 # formula
		while childOneIdx <= endIdx: # To check - if node doesn't have leaf or doesn't have anymore child
			childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1 # -1 is coz if childIdx doesn't have leaf
			if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
				idxToSwap = childTwoIdx
			else:
				idxToSwap = childOneIdx # if childOneIdx < childTwoIdx
			if heap[idxToSwap] < heap[currentIdx]:
				self.swap(currentIdx, idxToSwap, heap)
				currentIdx = idxToSwap # siftDown
				childOneIdx = currentIdx * 2 + 1 # recalculate 
			else:
				return	

    def siftUp(self, currentIdx, heap):
		parentIdx = (currentIdx - 1) // 2 #formula to check
		while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
			self.swap(currentIdx, parentIdx, heap)
			currentIdx = parentIdx
			parentIdx = (currentIdx - 1) // 2
			
    def peek(self):
		return self.heap[0] # peeking root node

    def remove(self):
		self.swap(0, len(self.heap) - 1, self.heap)#swapping the two value
		valueToRemove = self.heap.pop()
		self.siftDown(0, len(self.heap) - 1, self.heap)
		return valueToRemove # returning minimum value
		
    def insert(self, value):
		self.heap.append(value) # add the value 
		self.siftUp(len(self.heap) - 1, self.heap) # siftup = two values - current index & heap
		
	def swap(self, i, j, heap):
		heap[i], heap[j] = heap[j], heap[i]