# https://leetcode.com/problems/longest-continuous-increasing-subsequence/

import unittest

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = 1
        numsLength = len(nums)
		
        if numsLength < 2:
            answer = numsLength
        else:
			
            tmp = 1
			
            for i in range(numsLength - 1):
				
                if nums[i + 1] > nums[i]:
                    tmp += 1
                else:
                    tmp = 1
				
                if tmp > answer:
                    answer = tmp
		
        return answer

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
    
    def tearDown(self):
        pass

    def test_case_1(self):
        self.assertEqual(self.solution.findLengthOfLCIS([]), 0)

    def test_case_2(self):
        self.assertEqual(self.solution.findLengthOfLCIS([1]), 1)

    def test_case_3(self):
        self.assertEqual(self.solution.findLengthOfLCIS([1,3,5,4,7]), 3)

    def test_case_4(self):
        self.assertEqual(self.solution.findLengthOfLCIS([2,2,2,2,2]), 1)
    
if __name__ == '__main__':
    unittest.main()