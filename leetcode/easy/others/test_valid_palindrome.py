# https://leetcode.com/problems/valid-palindrome/

import unittest

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == None or s == "":
            return True
        
        i = 0
        j = len(s) - 1
        s = s.lower()
        
        while j > i:
            
            ci = s[i]
            cj = s[j]
            
            if False == ci.isalnum():
                i += 1
            elif False == cj.isalnum():
                j -= 1
            else:
                if ci != cj:
                    return False
                
                i += 1
                j -= 1
        
        return True
        
class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
    
    def tearDown(self):
        pass

    def test_case_1(self):
        self.assertTrue(self.solution.isPalindrome("A man, a plan, a canal: Panama"))

    def test_case_2(self):
        self.assertFalse(self.solution.isPalindrome("race a car"))

    def test_case_3(self):
        self.assertFalse(self.solution.isPalindrome("1a2"))

    def test_case_4(self):
        self.assertTrue(self.solution.isPalindrome(""))

if __name__ == '__main__':
    unittest.main()