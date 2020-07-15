# https://leetcode.com/problems/product-of-array-except-self/
#
# This is difficult, and I take a reference on this:
# https://www.programcreek.com/2014/07/leetcode-product-of-array-except-self-java/

import unittest
import json


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        numsLength = len(nums)
        answer = list()
        t1 = [1] * numsLength
        t2 = [1] * numsLength

        for i in range(1, numsLength):
            t1[i] = t1[i - 1] * nums[i - 1]

        for i in range(numsLength - 2, -1, -1):
            t2[i] = t2[i + 1] * nums[i + 1]

        for i in range(numsLength):
            answer.append(t1[i] * t2[i])

        return answer


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def test_case_1(self):
        self.assertEqual(self.solution.productExceptSelf([1, 2, 3]), [6, 3, 2])

    def test_case_2(self):
        self.assertEqual(
            self.solution.productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_case_3(self):

        filepath = "./leetcode/medium/others/"\
            + "test_product_of_array_except_self_case3.json"

        testData = None
        with open(filepath, "rt") as fout:
            testData = json.loads(fout.read())

        self.assertEqual(
            self.solution.productExceptSelf(testData["input"]),
            testData["answer"])


if __name__ == '__main__':
    unittest.main()
