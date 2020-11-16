# Going backwards
class Solution(object):
    def canJump(self, nums):
        goal = len(nums) - 1
        for i in range(len(nums))[::-1]:
            if i + nums[i] >= goal:
                goal = i
        return not goal

# Going forwards. 
class Solution(object):
    def canJump(self, nums):
        m = 0 # m tells the maximum index we can reach so far.
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i+n)
        return True
# ELP
def can_reach_end(A):
    furthest_reach_so_far, last_index = 0, len(A) - 1
    i = 0
    while i <= furthest_reach_so_far and furthest_reach_so_far < last_index:
        furthest_reach_so_far = max(furthest_reach_so_far, A[i] + i)
        i += 1
    return furthest_reach_so_far >= last_index