# https://leetcode.com/problems/unique-paths-ii/
# https://en.wikipedia.org/wiki/Dynamic_programming

import unittest


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        numOfRows = len(obstacleGrid)
        numOfColumns = len(obstacleGrid[0])

        dp = [[0] * numOfColumns for i in range(numOfRows)]

        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1

        for i in range(1, numOfRows):

            if obstacleGrid[i - 1][0] == 1:
                # re-label impossible moves
                obstacleGrid[i][0] = 1

            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1

        for j in range(1, numOfColumns):

            if obstacleGrid[0][j - 1] == 1:
                # re-label impossible moves
                obstacleGrid[0][j] = 1

            if obstacleGrid[0][j] == 0:
                dp[0][j] = 1

        for i in range(1, numOfRows):
            for j in range(1, numOfColumns):

                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                else:
                    dp[i][j] = 0

        return dp[numOfRows - 1][numOfColumns - 1]


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def test_case_1(self):
        self.assertEqual(self.solution.uniquePathsWithObstacles(
            [[0, 0, 0], [0, 1, 0], [0, 0, 0]]), 2)

    def test_case_2(self):
        self.assertEqual(self.solution.uniquePathsWithObstacles(
            [[0, 0], [0, 0], [0, 0], [1, 0], [0, 0]]), 3)


if __name__ == '__main__':
    unittest.main()
