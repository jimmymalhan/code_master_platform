# Going backwards
class Solution(object):
    def canJump(self, nums):
        last_position = len(nums) -1
        
        for i in range(len(nums)-2,-1,-1):
            if (i + nums[i]) >= last_position:
                last_position = i
        return last_position == 0