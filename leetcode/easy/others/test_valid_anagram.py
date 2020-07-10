# https://leetcode.com/problems/valid-anagram/

import unittest

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)
        
class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
    
    def tearDown(self):
        pass

    def test_case_1(self):
        self.assertTrue(self.solution.isAnagram("abcd", "dcab"))
    
    def test_case_2(self):
        self.assertTrue(self.solution.isAnagram("anagram", "nagaram"))
    
    def test_case_3(self):
        self.assertFalse(self.solution.isAnagram("rat", "car"))

if __name__ == '__main__':
    unittest.main()