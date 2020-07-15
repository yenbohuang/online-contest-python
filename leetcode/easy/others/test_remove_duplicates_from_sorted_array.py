# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

import unittest
import os
import json


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None:
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
        self.assertEqual(self.solution.removeDuplicates([1, 1, 2]), 2)

    def test_case_2(self):
        self.assertEqual(self.solution.removeDuplicates([1, 1, 2, 2, 3, 3]), 3)

    def test_case_3(self):

        filepath = os.path.abspath(".") + "/leetcode/easy/others/" \
            + "test_remove_duplicates_from_sorted_array_case3.json"

        testData = None
        with open(filepath, "rt") as fout:
            testData = json.loads(fout.read())

        self.assertEqual(self.solution.removeDuplicates(testData), 38)

    def test_case_4(self):
        self.assertEqual(self.solution.removeDuplicates(
            [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), 5)


if __name__ == '__main__':
    unittest.main()
