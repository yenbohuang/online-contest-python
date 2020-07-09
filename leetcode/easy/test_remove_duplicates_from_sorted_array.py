# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

import unittest

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None:
            return 0
        elif len(nums) <= 1:
            return len(nums)

        lastIndex = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                lastIndex += 1
                nums[lastIndex] = nums[i]

        return lastIndex + 1

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
    
    def tearDown(self):
        pass

    def test_case_1(self):
        self.assertEqual( \
            self.solution.removeDuplicates([1,1,2]), \
            2)

    def test_case_2(self):
        self.assertEqual( \
            self.solution.removeDuplicates([1,1,2,2,3,3]), \
            3)

    def test_case_3(self):
        self.assertEqual( \
            self.solution.removeDuplicates([-14,-14,-13,-13,-13,-13,-13,-13,-13,-12,-12,-12,-12,-11,-10,-9,-9,-9,-8,-7,-5,-5,-5,-5,-4,-3,-3,-2,-2,-2,-2,-1,-1,-1,-1,-1,0,1,1,1,1,2,2,2,3,3,3,4,4,4,4,5,5,5,6,6,6,6,7,8,8,8,9,9,9,10,10,10,11,11,11,12,12,12,13,14,14,14,14,15,16,16,16,18,18,18,19,19,19,19,20,20,20,21,21,21,21,21,21,22,22,22,22,22,23,23,24,25,25]), \
            38)

    def test_case_4(self):
        self.assertEqual( \
            self.solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]), \
            5)
    
if __name__ == '__main__':
    unittest.main()