# https://leetcode.com/problems/contains-duplicate/

import unittest
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums) # set() removes duplicates

class TestSolution(unittest.TestCase):
    def test_containsDuplicate(self):
        solution = Solution()
        self.assertEqual(solution.containsDuplicate([1,2,3,1]), True)
        self.assertEqual(solution.containsDuplicate([1,2,3,4]), False)
        self.assertEqual(solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]), True)

def main():
    unittest.main()

if __name__ == '__main__':
    main()