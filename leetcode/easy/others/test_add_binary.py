# https://leetcode.com/problems/add-binary/

import unittest
import json


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        maxLength = max(len(a), len(b))

        reverseAList = list(a.zfill(maxLength)[::-1])
        reverseBList = list(b.zfill(maxLength)[::-1])

        answer = ""
        increment = 0

        for i in range(maxLength):
            sum = increment + int(reverseAList[i]) + int(reverseBList[i])
            answer += str(sum % 2)
            increment = sum // 2

        while (increment > 0):
            answer += str(increment % 2)
            increment //= 2

        return answer[::-1]


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def test_case_1(self):
        self.assertEqual(self.solution.addBinary("11", "1"), "100")

    def test_case_2(self):

        filepath = "./leetcode/easy/others/test_add_binary_case2.json"

        testData = None
        with open(filepath, "rt") as fout:
            testData = json.loads(fout.read())

        self.assertEqual(
            self.solution.addBinary(testData["a"], testData["b"]),
            testData["answer"])


if __name__ == '__main__':
    unittest.main()
