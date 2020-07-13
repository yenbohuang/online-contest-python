# https://leetcode.com/problems/fibonacci-number/

import unittest


class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 1:
            return N

        array = [0, 1]

        for i in range(2, N + 1):
            array.append(array[i - 1] + array[i - 2])

        return array[N]


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def test_case_1(self):
        self.assertEqual(self.solution.fib(1), 1)

    def test_case_2(self):
        self.assertEqual(self.solution.fib(2), 1)

    def test_case_3(self):
        self.assertEqual(self.solution.fib(3), 2)

    def test_case_4(self):
        self.assertEqual(self.solution.fib(4), 3)

    def test_case_5(self):
        self.assertEqual(self.solution.fib(0), 0)


if __name__ == '__main__':
    unittest.main()
