# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

import unittest


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None:
            return 0
        elif len(nums) == 1:
            return 1

        n = len(nums)
        updated = True

        while updated:

            updated = False
            duplicated = 0

            for i in range(n - 1):

                if nums[i] == nums[i + 1]:

                    duplicated += 1

                    if duplicated > 1:

                        for j in range(i, n - 1):
                            nums[j] = nums[j+1]

                        n -= 1
                        updated = True
                        break

                else:
                    duplicated = 0

        return n


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def test_case_1(self):
        self.assertEqual(self.solution.removeDuplicates([1, 1, 1, 2, 2, 3]), 5)

    def test_case_2(self):
        self.assertEqual(self.solution.removeDuplicates(
            [0, 0, 1, 1, 1, 1, 2, 3, 3]), 7)


if __name__ == '__main__':
    unittest.main()
