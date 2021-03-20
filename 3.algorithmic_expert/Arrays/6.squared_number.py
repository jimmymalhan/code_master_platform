# O(nlogn) time | O(n) space - where n is the length of the array
# def sortedSquaredArray(array):
# 	sortedSquares = [0 for _ in array] 	# assigning 0 to every element in array
	
# 	for idx in range(len(array)):
# 		value = array[idx] # assigning every element in array
# 		sortedSquares[idx] = value * value
	
# 	sortedSquares.sort()
# 	return sortedSquares

# def sortedSquaredArray(array):
# 	squaredList = []
# 	for item in array:
# 		squaredList.append(item * item)
# 	squaredList.sort()
# 	return squaredList

def sortedSquaredArray(array):
	return (sorted(i ** 2 for i in array))