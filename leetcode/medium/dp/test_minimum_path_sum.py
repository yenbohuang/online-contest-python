# https://leetcode.com/problems/minimum-path-sum/
# https://en.wikipedia.org/wiki/Dynamic_programming

import unittest
import json


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid is None or len(grid) == 0:
            return 0

        width = len(grid[0])
        height = len(grid)

        dynamicProgramming = [[0] * width for i in range(height)]
        dynamicProgramming[0][0] = grid[0][0]

        # initialize top row
        for i in range(1, width):
            dynamicProgramming[0][i] = dynamicProgramming[0][i - 1] + grid[0][i]

        # initialize left column
        for j in range(1, height):
            dynamicProgramming[j][0] = dynamicProgramming[j - 1][0] + grid[j][0]

        # fill up the dynamic programming table
        for i in range(1, height):

            for j in range(1, width):

                if dynamicProgramming[i-1][j] > dynamicProgramming[i][j-1]:
                    dynamicProgramming[i][j] = dynamicProgramming[i][j-1] + grid[i][j]
                else:
                    dynamicProgramming[i][j] = dynamicProgramming[i-1][j] + grid[i][j]

        return dynamicProgramming[height-1][width-1]


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

        filepath = "./leetcode/medium/dp/test_minimum_path_sum_cases.json"
        with open(filepath, "rt") as fout:
            self.testData = json.loads(fout.read())

    def tearDown(self):
        pass

    def test_case_1(self):
        self.assertEqual(self.solution.minPathSum(None), 0)

    def test_case_2(self):
        self.assertEqual(self.solution.minPathSum([[1, 2], [1, 1]]), 3)

    def test_case_3(self):
        self.assertEqual(self.solution.minPathSum(
            [[1, 3, 1], [1, 5, 1], [4, 2, 1]]), 7)

    def test_case_4(self):
        self.assertEqual(self.solution.minPathSum(self.testData["case4"]), 47)

    def test_case_5(self):
        self.assertEqual(self.solution.minPathSum(self.testData["case5"]), 855)

    def test_case_6(self):
        self.assertEqual(self.solution.minPathSum(
            [[1, 3, 1], [1, 5, 1], [4, 2, 1]]), 7)


if __name__ == '__main__':
    unittest.main()
