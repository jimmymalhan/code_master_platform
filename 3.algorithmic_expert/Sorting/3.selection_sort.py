# divide arr: sorted arr with len of 0, 
# find smallest num in unsorted array, 
# insert it into sorted subarray with swap

# Best: O(n^2) time | O(1)space
# Average: O(n^2) time | O(1)space
# Worst: O(n^2) time | O(1)space

def selectionSort(array):
	currentIdx = 0 # sorted subarray with len 0
	while currentIdx < len(array) - 1: # finding smallest num in unsorted subarray
		smallestIdx = currentIdx # smallestidx is the 1st idx with value 0
		for i in range(currentIdx + 1, len(array)): # from 2nd idx to len(array)
			if array[smallestIdx] > array[i]: # if 1st idx(SMALLEST NUMBER) in the array > 2nd idx to end of the array(CURRENT NUMBER)
				smallestIdx = i # appending (idx) smallestIdx(0) to be i (currentIdx)
		swap(currentIdx, smallestIdx, array)
		currentIdx += 1
	return array

def swap(i, j, array):
	array[i], array[j] = array[j], array[i]