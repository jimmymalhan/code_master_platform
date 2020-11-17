class Solution(object):
    def removeDuplicates(self, nums):
        nums[:] = sorted(set(nums))
        return len(nums)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        w = 1
        for i in range(1, len(nums)):
            if nums[w -1] != nums[i]:
                nums[w] = nums[i]
                w += 1
        return w