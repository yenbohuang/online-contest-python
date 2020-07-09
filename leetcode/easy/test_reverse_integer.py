# https://leetcode.com/problems/reverse-integer/

import unittest

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        maxInteger = 2 ** 31 - 1
        minInteger = -2 ** 31
        if x < minInteger or x > maxInteger:
            return 0

        isNegative = (x < 0)

        if isNegative:
            x = -x
		
        newList = []

        while x > 0:
            newList.append(x % 10)
            x //= 10

        answer = 0

        for i in newList:
            answer = answer * 10 + i

        if x < (-2 ** 31) or x > (2 ** 31 - 1):
            return 0

        if isNegative:
            answer = -answer
            if answer < minInteger:
                return 0
        else:
            if answer > maxInteger:
                return 0
        
        return answer

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
    
    def tearDown(self):
        pass

    def test_case_1(self):
        self.assertEqual( \
            self.solution.reverse(123), \
            321)
    
    def test_case_2(self):
        self.assertEqual( \
            self.solution.reverse(-123), \
            -321)

    def test_case_3(self):
        self.assertEqual( \
            self.solution.reverse(120), \
            21)
    
    def test_case_4(self):
        self.assertEqual( \
            self.solution.reverse(1534236469), \
            0)
    
if __name__ == '__main__':
    unittest.main()