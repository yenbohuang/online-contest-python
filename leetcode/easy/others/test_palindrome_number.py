# https://leetcode.com/problems/palindrome-number/

import unittest


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        xString = str(x)
        return xString == xString[::-1]


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def test_case_1(self):
        self.assertTrue(self.solution.isPalindrome(121))

    def test_case_2(self):
        self.assertFalse(self.solution.isPalindrome(-121))

    def test_case_3(self):
        self.assertFalse(self.solution.isPalindrome(10))


if __name__ == '__main__':
    unittest.main()
