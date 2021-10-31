# import List
# from typing import List

class Solution:
    def smallestEqual(self, nums):
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                return i
        return -1

    def smallestEqual2(self, nums):
        for i, num in enumerate(nums):
            if i % 10 == nums:
                return i
        return -1


def main():
    nums = [4,3,2,1]
    print(Solution().smallestEqual2(nums))
    
import unittest
class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        self.assertEqual(s.smallestEqual([4,3,2,1]), 2)
        print("Tests Passed!")
    def test2(self):
        s = Solution()
        self.assertEqual(s.smallestEqual([4,3,2,1]), 2)
        print("Tests Passed!")

if __name__ == "__main__":
    unittest.main() 
    main()