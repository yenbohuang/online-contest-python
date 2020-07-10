# https://leetcode.com/problems/sqrtx/

# This is not easy, and I copied source codes from Wikipedia
# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots

import unittest

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        bit = 1 << 30 # The second-to-top bit is set: 1 << 30 for 32 bits

        # "bit" starts at the highest power of four <= the argument.
        while bit > x:
            bit >>= 2
	 
        while bit != 0:
            if x >= res + bit:
	            x -= res + bit
	            res = (res >> 1) + bit
            else:
                res >>= 1

            bit >>= 2

        return res

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
    
    def tearDown(self):
        pass

    def test_case_1(self):
        self.assertEqual(self.solution.mySqrt(3), 1)

    def test_case_2(self):
        self.assertEqual(self.solution.mySqrt(4), 2)

    def test_case_3(self):
        self.assertEqual(self.solution.mySqrt(5), 2)

    def test_case_4(self):
        self.assertEqual(self.solution.mySqrt(10), 3)

    def test_case_5(self):
        self.assertEqual(self.solution.mySqrt(2147483647), 46340)

    def test_case_6(self):
        self.assertEqual(self.solution.mySqrt(121), 11)

    def test_case_7(self):
        self.assertEqual(self.solution.mySqrt(8), 2)

if __name__ == '__main__':
    unittest.main()