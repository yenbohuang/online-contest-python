# https://leetcode.com/problems/plus-one/

import unittest

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits == None:
            return None
		
        answer = list(digits)
        answer[-1] += 1
		
        for i in range(len(answer) - 1, 0, -1):

            if answer[i] > 9:
                answer[i] -= 10
                answer[i - 1] += 1
		
        if answer[0] > 9:
            answer[0] -= 10
            answer.insert(0, 1)
		
        return answer

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
    
    def tearDown(self):
        pass

    def test_case_1(self):
        self.assertEqual(self.solution.plusOne([1, 2, 3]), [1, 2, 4])
    
    def test_case_2(self):
        self.assertEqual(self.solution.plusOne([9]), [1, 0])
    
    def test_case_3(self):
        self.assertEqual(self.solution.plusOne([4, 3, 2, 1]), [4, 3, 2, 2])
    
if __name__ == '__main__':
    unittest.main()