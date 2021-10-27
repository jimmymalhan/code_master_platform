# https://leetcode.com/problems/maximum-subarray/

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.
""" Note:
Kadane's Algorithm
"""
import unittest
from typing import List

class Solution:
    # O(n) time, O(1) space
    def maxSubArray(self, nums) -> int:
        max_sum, current_sum = -float('inf'), 0    
        for num in nums:   
            current_sum = max(num, current_sum + num) # if current_sum + num < 0, then current_sum = 0
            max_sum = max(current_sum, max_sum) # if current_sum > max_sum, then current_sum is the new max_sum    
        return max_sum

    # divide and conquer
    # O(nlogn) time, O(1) space

    def maxSubArray_divide_conquer(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        # if len(nums) == 0, return 0
        if len(nums) == 0:
            return 0
        # divide
        mid = len(nums) // 2 
        left_sum = self.maxSubArray_divide_conquer(nums[:mid])
        right_sum = self.maxSubArray_divide_conquer(nums[mid:])
        # conquer
        left_sum_max = nums[mid - 1] # nums[mid - 1] is the last element of left subarray
        left_sum_current = 0
        for i in range(mid - 1, -1, -1): # from mid - 1 to 0
            left_sum_current += nums[i] # sum up all the elements in left subarray
            left_sum_max = max(left_sum_max, left_sum_current) # if left_sum_current > left_sum_max, then left_sum_current is the new left_sum_max
        right_sum_max = nums[mid] # nums[mid] is the first element of right subarray
        right_sum_current = 0
        for i in range(mid, len(nums)): # from mid to len(nums) - 1
            right_sum_current += nums[i] # sum up all the elements in right subarray
            right_sum_max = max(right_sum_max, right_sum_current) # if right_sum_current > right_sum_max, then right_sum_current is the new right_sum_max
        return max(left_sum, right_sum, left_sum_max + right_sum_max)

    # dynamic programming
    # O(n) time, O(1) space
    def maxSubArray_dynamic_programming(self, nums: List[int]) -> int:
        best = nums[0]
        current = nums[0]
        for i in nums[1:]:
            current = max(i, current + i)
            if current > best:
                best = current
        return best


class Test(unittest.TestCase):
    def test(self):
        test = Solution()
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        self.assertEqual(test.maxSubArray(nums), 6)
    def test_divide_conquer(self):
        test = Solution()
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        self.assertEqual(test.maxSubArray_divide_conquer(nums), 6)
    def test_dynamic_programming(self):
        test = Solution()
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        self.assertEqual(test.maxSubArray_dynamic_programming(nums), 6)

def main():
    unittest.main()

if __name__ == "__main__":
    main()