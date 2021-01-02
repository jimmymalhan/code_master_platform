# O(log(n)) time | O(log(n)) space
def binarySearch(array, target):
	return binarySearchHelper(array, target, 0, len(array) - 1)

def binarySearchHelper(array, target, left, right):
	if left > right:
        return - 1 # if number is not found return -1
    middle = (left + right) // 2
    potentialMatch = array[middle]
    if target == potentialMatch:
        return middle
    elif target < potentialMatch:
	    return binarySearchHelper(array, target, left, middle - 1) # middle -1 = right pointer # eliminating the entire right half of an array, move right pointer one position to the left of the middle pointer
    else: # target > potentialMatch
	    return binarySearchHelper(array, target, middle + 1, right) # eliminate the left half of an array, move left pointer one position to the right of the middle pointer

# O(log(n)) time | O(1) space
def binarySearch(array, target):
	return binarySearchHelper(array, target, 0, len(array) - 1)

def binarySearchHelper(array, target, left, right):
	while left <= right:
		middle = (left + right) // 2
		potentialMatch = array[middle]
		if target == potentialMatch:
			return middle
		elif target < potentialMatch:
			right = middle - 1
		else:
			left = middle + 1
	return -1