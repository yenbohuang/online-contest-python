# https://leetcode.com/problems/merge-intervals/

import unittest
from ...leetcode_intervals import IntervalQuestions


class Solution(IntervalQuestions):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        answer = list(list())

        intervalLength = 0
        if intervals is not None:
            intervalLength = len(intervals)

        if intervalLength == 0:
            return list(list())
        elif intervalLength < 2:
            answer.extend(intervals)
        else:
            intervals.sort(key=lambda x: (x[0], x[1]))

            current = intervals[0]
            answer.append(current)

            for i in range(1, intervalLength):

                if self.overlap(current, intervals[i]):

                    if intervals[i][0] < current[0]:
                        current[0] = intervals[i][0]

                    if intervals[i][1] > current[1]:
                        current[1] = intervals[i][1]
                else:
                    current = intervals[i]
                    answer.append(current)

        return answer


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def test_case_1(self):
        self.assertEqual(
            self.solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]),
            [[1, 6], [8, 10], [15, 18]])

    def test_case_2(self):
        self.assertEqual(
            self.solution.merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]),
            [[1, 10]])

    def test_case_3(self):
        self.assertEqual(
            self.solution.merge(
                [[2, 3], [2, 2], [3, 3], [1, 3], [5, 7], [2, 2], [4, 6]]),
            [[1, 3], [4, 7]])

    def test_case_4(self):
        self.assertEqual(self.solution.merge(list(list())), list(list()))


if __name__ == '__main__':
    unittest.main()
