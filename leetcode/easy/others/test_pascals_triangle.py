# https://leetcode.com/problems/pascals-triangle/

import unittest


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]

        answer = [[1], [1, 1]]

        for i in range(2, numRows):
            answer.append([1] * (i + 1))

            for j in range(1, i):
                answer[i][j] = answer[i - 1][j - 1] + answer[i - 1][j]

        return answer


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def test_case_1(self):
        self.assertEqual(self.solution.generate(5),
                         [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1],
                         [1, 4, 6, 4, 1]])

    def test_case_2(self):
        self.assertEqual(self.solution.generate(0), [])

if __name__ == '__main__':
    unittest.main()
