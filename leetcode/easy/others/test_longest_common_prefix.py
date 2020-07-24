# https://leetcode.com/problems/longest-common-prefix/

import unittest


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""

        answer = ""
        strLength = len(strs[0])

        try:
            for i in range(strLength):
                found = True
                candidate = strs[0][i]

                for s in strs:
                    if s[i] != candidate:
                        found = False
                        break

                if found:
                    answer += candidate
                else:
                    break
        except IndexError:
            pass

        return answer


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def test_case_1(self):
        self.assertEqual(self.solution.longestCommonPrefix(
            ["flower", "flow", "flight"]), "fl")

    def test_case_2(self):
        self.assertEqual(self.solution.longestCommonPrefix(
            ["dog", "racecar", "car"]), "")

    def test_case_3(self):
        self.assertEqual(self.solution.longestCommonPrefix(
            ["abcd", "abc", "ab"]), "ab")

    def test_case_4(self):
        self.assertEqual(self.solution.longestCommonPrefix([]), "")


if __name__ == '__main__':
    unittest.main()
