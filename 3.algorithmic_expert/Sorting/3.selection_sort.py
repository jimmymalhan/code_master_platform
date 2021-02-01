# Concept - Find the smallest number in the array and swap it with the first element

# Best: O(n^2) time | O(1)space
# Average: O(n^2) time | O(1)space
# Worst: O(n^2) time | O(1)space

def selectionSort(array):
	currentIdx = 0
	while currentIdx < len(array) - 1:
		smallestIdx = currentIdx # value is 0
		for i in range(currentIdx + 1, len(array)):
			if array[smallestIdx] > array[i]: # if 0 > currentNumber- array[i]
				smallestIdx = i # append smallestIdx to be i
		swap(currentIdx, smallestIdx, array)
		currentIdx += 1
	return array

def swap(i, j, array):
	array[i], array[j] = array[j], array[i]