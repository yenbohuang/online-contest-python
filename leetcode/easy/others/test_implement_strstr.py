# https://leetcode.com/problems/implement-strstr/

import unittest

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == None or needle == None:
            return -1

        haystackLength = len(haystack)
        needleLength = len(needle)

        if haystackLength < needleLength:
            return -1

        if needleLength == 0:
            return 0

        firstChar = needle[0]

        for i in range(0, haystackLength):

            if haystack[i] == firstChar:

                exactMatch = True

                for j in range(0, needleLength):

                    if needle[j] != haystack[i + j]:
                        exactMatch = False
                        break
				
                if exactMatch:
                    return i
			
            if haystackLength - i - 1 < needleLength:
                break

        return -1

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
    
    def tearDown(self):
        pass

    def test_case_1(self):
        self.assertEqual(self.solution.strStr("source", "target"), -1)
    
    def test_case_2(self):
        self.assertEqual(self.solution.strStr("abcdabcdefg", "bcd"), 1)
    
    def test_case_3(self):
        self.assertEqual(self.solution.strStr("", ""), 0)
    
    def test_case_4(self):
        self.assertEqual(self.solution.strStr("a", ""), 0)
    
    def test_case_5(self):
        self.assertEqual(self.solution.strStr("hello", "ll"), 2)

    def test_case_6(self):
        self.assertEqual(self.solution.strStr("aaaaa", "bba"), -1)

    def test_case_7(self):
        self.assertEqual(self.solution.strStr("mississippi", "sippia"), -1)

    def test_case_8(self):
        self.assertEqual(self.solution.strStr("a", "a"), 0)

    def test_case_9(self):
        self.assertEqual(self.solution.strStr("mississippi", "pi"), 9)

if __name__ == '__main__':
    unittest.main()