# https://leetcode.com/problems/reverse-words-in-a-string/

import unittest


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None:
            return None

        s = s.strip()

        if len(s) == 0:
            return s

        tokens = s.split(" ")
        answer = ""

        for t in tokens:

            if len(t.strip()) > 0:
                answer = t + " " + answer

        return answer.strip()


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def test_case_1(self):
        self.assertEqual(self.solution.reverseWords(
            "the sky is blue"), "blue is sky the")

    def test_case_2(self):
        self.assertEqual(self.solution.reverseWords(
            "  hello world!  "), "world! hello")

    def test_case_3(self):
        self.assertEqual(self.solution.reverseWords(
            "a good   example"), "example good a")


if __name__ == '__main__':
    unittest.main()
