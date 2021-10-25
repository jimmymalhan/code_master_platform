class Solutions:
	# O(n^2) time | O(1) space
	def twoNumberSum1(self, array, targetSum):
		for i in range(len(array) - 1):
			for j in range(i + 1, len(array)):
				if array[i] + array[j] == targetSum:
					return [array[i], array[j]]
		return[]

	# O(n) time | O(1) space
	def twoNumberSum2(self, array, targetSum):
		nums = {}
		for num in array:
			potentialMatch = targetSum - num
			if potentialMatch in numDict:
				return [potentialMatch, num]
			else:
				nums[num] = True
		return []
	# Time O(nlog(n)) | O(1) space
	def twoNumberSum3(self, array, targetSum):
		array.sort()
		left = 0
		right = len(array) - 1
		while left < right:
			currentSum = array[left] + array[right]
			if currentSum == targetSum:
				return [array[left], array[right]]
			elif currentSum < targetSum:
				left += 1
			elif currentSum > targetSum:
				right -= 1
		return []

import unittest
class Test(unittest.TestCase):
	def test_twoNumberSum1(self):
		s = Solutions()
		self.assertEqual(s.twoNumberSum1([3, 5,-4, 8, 11, 1, -1, 6], 10), [11, -1])
	def test_twoNumberSum2(self):
		s = Solutions()
		self.assertEqual(s.twoNumberSum1([3, 5,-4, 8, 11, 1, -1, 6], 10), [11, -1])
	def test_twoNumberSum3(self):
		s = Solutions()
		self.assertEqual(s.twoNumberSum1([3, 5,-4, 8, 11, 1, -1, 6], 10), [11, -1])

def main():
	unittest.main()

if __name__ == '__main__':
	main()