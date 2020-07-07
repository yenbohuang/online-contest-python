# https://leetcode.com/problems/length-of-last-word/

import unittest

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        answer = 0
		
        if len(s.strip()) > 0:
            tokens = s.strip().split(" ")
            answer = len(tokens[len(tokens) - 1])
		
        return answer

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
    
    def tearDown(self):
        pass

    def test_case_1(self):
        self.assertEqual( \
            self.solution.lengthOfLastWord("Hello World"), \
            5)
    
    if __name__ == '__main__':
        unittest.main()