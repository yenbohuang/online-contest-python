# https://leetcode.com/problems/count-and-say/

import unittest


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        answer = "1"

        for i in range(1, n):

            tmp = ""
            count = 0
            answerLength = len(answer)

            for j in range(answerLength):

                if j == 0:
                    count = 1
                elif answer[j] == answer[j - 1]:
                    count += 1
                else:
                    tmp += str(count) + answer[j - 1]
                    count = 1

            answer = tmp + str(count) + answer[-1]

        return answer


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def test_case_1(self):
        self.assertEqual(self.solution.countAndSay(1), "1")

    def test_case_2(self):
        self.assertEqual(self.solution.countAndSay(2), "11")

    def test_case_3(self):
        self.assertEqual(self.solution.countAndSay(3), "21")

    def test_case_4(self):
        self.assertEqual(self.solution.countAndSay(4), "1211")

    def test_case_5(self):
        self.assertEqual(self.solution.countAndSay(5), "111221")


if __name__ == '__main__':
    unittest.main()
