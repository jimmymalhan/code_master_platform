# You are given a 0-indexed integer array nums. The array nums is beautiful if:

# nums.length is even.
# nums[i] != nums[i + 1] for all i % 2 == 0.
# Note that an empty array is considered beautiful.

# You can delete any number of elements from nums. When you delete an element, all the elements to the right of the deleted element will be shifted one unit to the left to fill the gap created and all the elements to the left of the deleted element will remain unchanged.

# Return the minimum number of elements to delete from nums to make it beautiful.

# Input: nums = [1,1,2,3,5]
# Output: 1
# Explanation: You can delete either nums[0] or nums[1] to make nums = [1,2,3,5] which is beautiful. It can be proven you need at least 1 deletion to make nums beautiful.

# Input: nums = [1,1,2,2,3,3]
# Output: 2
# Explanation: You can delete nums[0] and nums[5] to make nums = [1,2,2,3] which is beautiful. It can be proven you need at least 2 deletions to make nums beautiful.

from typing import List
import collections
import itertools

class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        j = 0 # 
        i = 0 # i is the index of nums
        delete = 0 # delete is the number of deletions
        n = len(nums) # n is the length of nums
        while i < n: # while i is less than the length of nums
            if (i+1 < n and nums[i] == nums[i+1] and j%2 == 0) : # if i+1 is less than the length of nums and nums[i] is equal to nums[i+1] and j is even # it means that the next element is equal to the current element and the number of deletions is even
                delete += 1; # increment the number of deletions
            else:
                j += 1; #
            i += 1 # increment i
        if j%2 != 0: # if j is not even
            delete += 1 # increment the number of deletions
        return delete # return the number of deletions

print(Solution().minDeletion([1,1,2,3,5])) # 1
print(Solution().minDeletion([1,1,2,2,3,3])) # 2