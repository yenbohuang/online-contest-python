# https://leetcode.com/problems/rotate-string/

import unittest

class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A == B:
            return True
        elif len(A) == len(B):

            length = len(A)

            for i in range(length):

                target = A[i]
				
                index = B.find(target)

                while index != -1:

                    newBString = B[index:] + B[0:index]

                    if A == newBString:
                        return True

                    if index + 1 < length:
                        index = B.find(target, index + 1)
                    else:
                        break
		
        return False

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
    
    def tearDown(self):
        pass

    def test_case_1(self):
        self.assertTrue(self.solution.rotateString("abcde", "cdeab"))

    def test_case_2(self):
        self.assertFalse(self.solution.rotateString("abcde", "abced"))

    def test_case_3(self):
        self.assertTrue(self.solution.rotateString("", ""))

if __name__ == '__main__':
    unittest.main()