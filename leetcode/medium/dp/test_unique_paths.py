# https://leetcode.com/problems/unique-paths/
# https://en.wikipedia.org/wiki/Dynamic_programming

import unittest


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * m for i in range(n)]

        # column
        for i in range(n):
            dp[i][0] = 1

        # row
        for j in range(m):
            dp[0][j] = 1

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[n-1][m-1]


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def test_case_1(self):
        self.assertEqual(self.solution.uniquePaths(3, 2), 3)

    def test_case_2(self):
        self.assertEqual(self.solution.uniquePaths(7, 3), 28)


if __name__ == '__main__':
    unittest.main()
