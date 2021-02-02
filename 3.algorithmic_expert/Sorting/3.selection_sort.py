# Concept - create a smallest number(as idx), append it with the idx(bigger idx) and swap it (with the first element)

# Best: O(n^2) time | O(1)space
# Average: O(n^2) time | O(1)space
# Worst: O(n^2) time | O(1)space

def selectionSort(array):
	currentIdx = 0 #starting point
	while currentIdx < len(array) - 1:
		smallestIdx = currentIdx # (smallestidx is the first 1st idx) # value is 0
		for i in range(currentIdx + 1, len(array)): # from 2nd idx to len(array)
			if array[smallestIdx] > array[i]: # if 1st element(SMALLEST NUMBER) in the array > 2nd element to end of the array(CURRENT NUMBER)
				smallestIdx = i # appending (idx) smallestIdx(0) to be i (currentIdx)
		swap(currentIdx, smallestIdx, array)
		currentIdx += 1
	return array

def swap(i, j, array):
	array[i], array[j] = array[j], array[i]