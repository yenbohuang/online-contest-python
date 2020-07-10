# https://leetcode.com/problems/maximum-subarray/

import unittest
import sys

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxValue = -sys.maxsize
        numsLength = len(nums)
		
        for i in range(numsLength):
			
            sumValue = 0
			
            for j in range (i, numsLength):
				
                sumValue += nums[j]
				
                if sumValue > maxValue:
                    maxValue = sumValue
		
        return maxValue
        
class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
    
    def tearDown(self):
        pass

    def test_case_1(self):
        self.assertEqual(self.solution.maxSubArray([-2,2,-3,4,-1,2,1,-5,3]), 6)
    
    def test_case_2(self):
        self.assertEqual(self.solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]), 6)

    def test_case_3(self):
        self.assertEqual(self.solution.maxSubArray([-2147483647]), -2147483647)

if __name__ == '__main__':
    unittest.main()