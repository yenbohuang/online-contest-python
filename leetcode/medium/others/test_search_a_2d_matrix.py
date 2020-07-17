# https://leetcode.com/problems/search-a-2d-matrix/

import unittest


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix is None or len(matrix) == 0:
            return False

        for row in matrix:

            if row is None or len(row) == 0:
                continue
            elif row[0] == target:
                return True
            elif row[0] > target:
                return False
            elif row[0] < target:

                for n in row:
                    if n == target:
                        return True

        return False


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def test_case_1(self):
        self.assertTrue(
            self.solution.searchMatrix(
                [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]],
                3))

    def test_case_2(self):
        self.assertFalse(
            self.solution.searchMatrix(
                [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]],
                13))

    def test_case_3(self):
        self.assertFalse(self.solution.searchMatrix(list(list()), 1))


if __name__ == '__main__':
    unittest.main()
