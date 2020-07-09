# https://leetcode.com/problems/climbing-stairs/
#
# This one is not easy. So, I Googled. :p
# http://www.glassdoor.com/Interview/You-are-climbing-a-stair-case-Each-time-you-can-either-make-1-step-or-2-steps-The-staircase-has-n-steps-In-how-many-dist-QTN_133071.htm

import unittest

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Fibonacci
        if n <= 2:
            return n
        
        steps = [0, 1, 2]
        
        for i in range(3, n + 1):
            steps.append(steps[i - 1] + steps[i - 2])

        return steps[n]

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
    
    def tearDown(self):
        pass

    def test_case_1(self):
        self.assertEqual( \
            self.solution.climbStairs(3), \
            3)

if __name__ == '__main__':
    unittest.main()