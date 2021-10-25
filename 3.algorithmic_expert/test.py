from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        left = 0
        right = len(nums) - 1
        while left < right:
            if (nums[left] + nums[right]) == target:
                return [left, right] # nums[left], nums[right] = 2,4 - picked up the numbers correctly
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
        return []

if __name__ == '__main__':
    nums = [3, 2, 4]
    target = 6
    solution = Solution()
    print(solution.twoSum(nums, target))
# fails for this test case - [3, 2, 4], 6), [1, 2]

# Output = [0,2] should be [1,2]

# looks like it picks up the correct numbers but when it returns the index that's where it messes up