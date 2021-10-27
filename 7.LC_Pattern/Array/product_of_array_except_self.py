# https://leetcode.com/problems/product-of-array-except-self/

from typing import List
# O(n) time, O(n) space
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1 for _ in range(len(nums))]
        
        leftRunningProduct = 1
        for i in range(len(nums)):
            products[i] = leftRunningProduct
            leftRunningProduct *= nums[i]
            
        rightRunningProduct = 1
        for i in reversed(range(len(nums))):
            products[i] *= rightRunningProduct
            rightRunningProduct *= nums[i]
            
        return products

def main():
    sol = Solution()
    print(sol.productExceptSelf([1,2,3,4]))

if __name__ == "__main__":
    main()