# https://leetcode.com/problems/two-sum/

import unittest

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        size = len(nums)

        for i in range(0, size):

            for j in range(i + 1, size):

                if target == nums[i] + nums[j]:
                    return [i, j]

        return None
        
class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
    
    def tearDown(self):
        pass

    def test_case_1(self):
        self.assertEqual(self.solution.twoSum([2, 7, 11, 15], 9), [0,1])
    
    def test_case_2(self):
        self.assertEqual(self.solution.twoSum([2,5,5,11], 10), [1,2])

if __name__ == '__main__':
    unittest.main()