# https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/
# Input: nums = [5,1,3]
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        for i in range(n - 1):
            if nums[i] != nums[i + 1]:
                count += n-1-i
        return count