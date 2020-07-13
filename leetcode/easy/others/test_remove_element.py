# https://leetcode.com/problems/remove-element/

import unittest


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if nums is None:
            return 0

        answer = []

        for a in nums:

            if a != val:
                answer.append(a)

        answerSize = len(answer)

        for i in range(answerSize):
            nums[i] = answer[i]

        return answerSize


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def test_case_1(self):
        self.assertEqual(self.solution.removeElement(
            [0, 4, 4, 0, 0, 2, 4, 4], 4), 4)

    def test_case_2(self):
        self.assertEqual(self.solution.removeElement([3, 2, 2, 3], 3), 2)

    def test_case_3(self):
        self.assertEqual(self.solution.removeElement(
            [0, 1, 2, 2, 3, 0, 4, 2], 2), 5)


if __name__ == '__main__':
    unittest.main()
