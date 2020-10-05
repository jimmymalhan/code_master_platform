# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

nums = [2,7,11,15]; target = 9

class Solution(object):
    def twoSum(self):
        dic = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in dic:
                return [dic[m], i]
            else:
                dic[n] = i

if __name__ == '__main__':
    s = Solution()
    s.twoSum()
    print (s.twoSum())