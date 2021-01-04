def threeNumberSum(array, targetSum):
	array.sort()
	triplets = []
	for i in range(len(array) - 2):# array[i]/currentNumber is the first element of an array
		left = i + 1
		right = len(array) - 1
		while left < right:
			currentSum = array[i] + array[left] + array[right] #formula
			if currentSum == targetSum:
				triplets.append([array[i], array[left], array[right]])
				left += 1
				right -= 1
			elif currentSum < targetSum:
				left += 1
			elif currentSum > targetSum:
				right -= 1
	return triplets