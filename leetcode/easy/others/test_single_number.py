# https://leetcode.com/problems/single-number/

import unittest


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or not nums:
            return 0

        singleIntegers = {nums[0]}
        multipleIntegers = set()

        for i in range(1, len(nums)):

            if nums[i] in singleIntegers:
                singleIntegers.remove(nums[i])
                multipleIntegers.add(nums[i])
            elif False == (nums[i] in multipleIntegers):
                singleIntegers.add(nums[i])

        if not singleIntegers:
            return 0
        else:
            return singleIntegers.pop()


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def test_case_1(self):
        self.assertEqual(self.solution.singleNumber([1, 2, 2, 1, 3, 4, 3]), 4)

    def test_case_2(self):
        self.assertEqual(self.solution.singleNumber([2, 2, 1]), 1)

    def test_case_3(self):
        self.assertEqual(self.solution.singleNumber([4, 1, 2, 1, 2]), 4)


if __name__ == '__main__':
    unittest.main()
