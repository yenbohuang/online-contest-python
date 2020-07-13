# https://leetcode.com/problems/roman-to-integer/

import unittest

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            raise Exception("Invalid s: " + s)
		
        tmp = s
        answer = 0

        while len(tmp) > 0:

            if tmp.startswith("IV"):
                answer += 4
                tmp = tmp[2:]
            elif tmp.startswith("IX"):
                answer += 9
                tmp = tmp[2:]
            elif tmp.startswith("XL"):
                answer += 40
                tmp = tmp[2:]
            elif tmp.startswith("XC"):
                answer += 90
                tmp = tmp[2:]
            elif tmp.startswith("CD"):
                answer += 400
                tmp = tmp[2:]
            elif tmp.startswith("CM"):
                answer += 900
                tmp = tmp[2:]
            elif tmp.startswith("I"):
                answer += 1
                tmp = tmp[1:]
            elif tmp.startswith("V"):
                answer += 5
                tmp = tmp[1:]
            elif tmp.startswith("X"):
                answer += 10
                tmp = tmp[1:]
            elif tmp.startswith("L"):
                answer += 50
                tmp = tmp[1:]
            elif tmp.startswith("C"):
                answer += 100
                tmp = tmp[1:]
            elif tmp.startswith("D"):
                answer += 500
                tmp = tmp[1:]
            elif tmp.startswith("M"):
                answer += 1000
                tmp = tmp[1:]
        
        return answer

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
    
    def tearDown(self):
        pass

    def test_case_1(self):
        self.assertEqual(self.solution.romanToInt("IV"), 4)

    def test_case_2(self):
        self.assertEqual(self.solution.romanToInt("XXI"), 21)

    def test_case_3(self):
        self.assertEqual(self.solution.romanToInt("XCIX"), 99)

if __name__ == '__main__':
    unittest.main()