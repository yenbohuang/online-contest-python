# https://leetcode.com/problems/integer-to-roman/

import unittest


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        answer = ""

        while num // 1000 > 0:
            answer += "M"
            num -= 1000

        while num // 900 > 0:
            answer += "CM"
            num -= 900

        while num // 500 > 0:
            answer += "D"
            num -= 500

        while num // 400 > 0:
            answer += "CD"
            num -= 400

        while num // 100 > 0:
            answer += "C"
            num -= 100

        while num // 90 > 0:
            answer += "XC"
            num -= 90

        while num // 50 > 0:
            answer += "L"
            num -= 50

        while num // 40 > 0:
            answer += "XL"
            num -= 40

        while num // 10 > 0:
            answer += "X"
            num -= 10

        while num // 9 > 0:
            answer += "IX"
            num -= 9

        while num // 5 > 0:
            answer += "V"
            num -= 5

        while num // 4 > 0:
            answer += "IV"
            num -= 4

        while num > 0:
            answer += "I"
            num -= 1

        return answer


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def test_case_1(self):
        self.assertEqual(self.solution.intToRoman(4), "IV")

    def test_case_2(self):
        self.assertEqual(self.solution.intToRoman(21), "XXI")

    def test_case_3(self):
        self.assertEqual(self.solution.intToRoman(99), "XCIX")


if __name__ == '__main__':
    unittest.main()
