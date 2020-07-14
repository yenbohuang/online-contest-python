# https://leetcode.com/problems/insert-interval/

import unittest
from ...leetcode_intervals import IntervalQuestions


class Solution(IntervalQuestions):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        result = list(list())

        intervalsLength = 0
        if intervals is not None:
            intervalsLength = len(intervals)

        if intervalsLength == 0:

            result.append(newInterval)

        elif intervals[0][0] > newInterval[1]:

            result.append(newInterval)
            result.extend(intervals)

        elif intervals[-1][1] < newInterval[0]:

            result.extend(intervals)
            result.append(newInterval)

        else:

            for i in intervals:

                if self.overlap(i, newInterval):

                    if i[0] < newInterval[0]:
                        newInterval[0] = i[0]

                    if i[1] > newInterval[1]:
                        newInterval[1] = i[1]

                    if newInterval not in result:
                        result.append(newInterval)

                elif i[1] < newInterval[0]:

                    result.append(i)

                else:

                    if newInterval not in result:
                        result.append(newInterval)

                    result.append(i)

        return result


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def test_case_1(self):
        self.assertEqual(
            self.solution.insert([[1, 2], [5, 9]], [2, 5]),
            [[1, 9]])

    def test_case_2(self):
        self.assertEqual(
            self.solution.insert([[1, 2], [5, 9]], [3, 4]),
            [[1, 2], [3, 4], [5, 9]])

    def test_case_3(self):
        self.assertEqual(
            self.solution.insert(list(list()), [5, 7]),
            [[5, 7]])

    def test_case_4(self):
        self.assertEqual(
            self.solution.insert([[1, 5]], [2, 3]),
            [[1, 5]])

    def test_case_5(self):
        self.assertEqual(
            self.solution.insert([[1, 5]], [2, 7]),
            [[1, 7]])

    def test_case_6(self):
        self.assertEqual(
            self.solution.insert([[1, 5]], [1, 7]),
            [[1, 7]])

    def test_case_7(self):
        self.assertEqual(
            self.solution.insert([[1, 5], [7, 8], [10, 13]], [9, 9]),
            [[1, 5], [7, 8], [9, 9], [10, 13]])

    def test_case_8(self):
        self.assertEqual(
            self.solution.insert([[1, 3], [6, 9]], [2, 5]),
            [[1, 5], [6, 9]])

    def test_case_9(self):
        self.assertEqual(
            self.solution.insert(
                [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]),
            [[1, 2], [3, 10], [12, 16]])


if __name__ == '__main__':
    unittest.main()
