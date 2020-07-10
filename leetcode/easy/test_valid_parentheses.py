# https://leetcode.com/problems/valid-parentheses/

import unittest

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == None or len(s) % 2 == 1:
            return False
        elif len(s) == 0:
            return True
        
        # incorrect start or end
        if s[0] in ")]}" or s[-1] in "([{":
            return False
        
        stack = list()
        
        for c in list(s):
            
            if c == ')':
                
                if '(' != stack.pop():
                    return False
                
            elif c == '}':
                
                if '{' != stack.pop():
                    return False
                
            elif c == ']':
                
                if '[' != stack.pop():
                    return False
                
            else:
                stack.append(c)
        
        return True
        
class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
    
    def tearDown(self):
        pass

    def test_case_1(self):
        self.assertTrue(self.solution.isValid("()"))
    
    def test_case_2(self):
        self.assertTrue(self.solution.isValid("()[]{}"))
    
    def test_case_3(self):
        self.assertFalse(self.solution.isValid("(]"))
    
    def test_case_4(self):
        self.assertFalse(self.solution.isValid("([)]"))
    
    def test_case_5(self):
        self.assertTrue(self.solution.isValid("([])"))
    
    def test_case_6(self):
        self.assertFalse(self.solution.isValid("[])"))
    
    def test_case_7(self):
        self.assertTrue(self.solution.isValid("[{()}]"))
    
    def test_case_8(self):
        self.assertFalse(self.solution.isValid("[([]])"))

if __name__ == '__main__':
    unittest.main()