# https://leetcode.com/problems/search-insert-position/

import unittest

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if (nums == None) or (len(nums) == 0) or (nums[0] >= target):
            return 0

        numsLength = len(nums)
        for i in range(1, numsLength):

            if nums[i] >= target:
                return i

        return numsLength

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
    
    def tearDown(self):
        pass

    def test_case_1(self):
        self.assertEqual( \
            self.solution.searchInsert([1,3,5,6], 5), \
            2)

    def test_case_2(self):
        self.assertEqual( \
            self.solution.searchInsert([1,3,5,6], 2), \
            1)

    def test_case_3(self):
        self.assertEqual( \
            self.solution.searchInsert([1,3,5,6], 7), \
            4)

    def test_case_4(self):
        self.assertEqual( \
            self.solution.searchInsert([1,3,5,6], 0), \
            0)

if __name__ == '__main__':
    unittest.main()