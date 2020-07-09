# https://leetcode.com/problems/power-of-two/

import unittest

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 0:

            if n == 1:
                return True
            elif n % 2 != 0:
                return False
            else:
                n /= 2

        return False

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
    
    def tearDown(self):
        pass

    def test_case_1(self):
        self.assertTrue(self.solution.isPowerOfTwo(4))

    def test_case_2(self):
        self.assertFalse(self.solution.isPowerOfTwo(5))

    def test_case_3(self):
        self.assertTrue(self.solution.isPowerOfTwo(1024))

    def test_case_4(self):
        self.assertFalse(self.solution.isPowerOfTwo(-1))

    def test_case_5(self):
        self.assertTrue(self.solution.isPowerOfTwo(1))

    def test_case_6(self):
        self.assertTrue(self.solution.isPowerOfTwo(16))

    def test_case_7(self):
        self.assertFalse(self.solution.isPowerOfTwo(218))
    
if __name__ == '__main__':
    unittest.main()
