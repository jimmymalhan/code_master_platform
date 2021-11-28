# Find Target Indices After Sorting Array
# You are given a 0-indexed integer array nums and a target element target.

# A target index is an index i such that nums[i] == target.

# Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

# sample input 1:
# nums = [1,2,5,2,3], target = 2

# sample output:
# [1, 2]

# sample input 2:
# Input: nums = [1,2,5,2,3], target = 3

# sample output:
# Output: [3]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The index where nums[i] == 3 is 3.

from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        count = 0 
        result = [] 
        for i in range(len(nums)): # loop through nums
            if sorted_nums[i] == target:
                result.append(count)
            count += 1
        return result

def main():
    nums = [1,2,5,2,3]
    target = 2
    print(Solution().targetIndices(nums, target))

main()  

