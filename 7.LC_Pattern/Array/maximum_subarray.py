# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.
""" Note:
Kadane's Algorithm
"""

# O(n) time, O(1) space
class Solution:
    def maxSubArray(self, nums) -> int:
        max_sum, current_sum = -float('inf'), 0    
        for num in nums:   
            current_sum = max(num, current_sum + num) # if nums > current_sum + nums, then current_sum + nums is the new current_sum
            max_sum = max(current_sum, max_sum) # if current_sum > max_sum, then current_sum is the new max_sum    
        return max_sum

import unittest
class Test(unittest.TestCase):
    def test(self):
        test = Solution()
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        self.assertEqual(test.maxSubArray(nums), 6)
    def test2(self):
        test = Solution()
        nums = [-2,1]
        self.assertEqual(test.maxSubArray(nums), 1)
def main():
    unittest.main()

if __name__ == "__main__":
    main()