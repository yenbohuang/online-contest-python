# https://leetcode.com/problems/binary-search/

import unittest

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        answer = -1
        numsLength = len(nums)

        if 1 == numsLength:
            if target == nums[0]:
                answer = 0
        elif target == nums[0]:
            answer = 0
        elif target == nums[-1]:
            answer = numsLength - 1
        else:
            start = 0
            end = numsLength - 1
            prevStart = -1
            prevEnd = -1

            while start != end:

                if prevStart == start and prevEnd == end:
                    break

                prevStart = start
                prevEnd = end

                mid = (start + end) // 2

                if target == nums[mid]:

                    if 0 == mid or target > nums[mid - 1]:
                        answer = mid
                        break
                    else:
                        end = mid
                elif target > nums[mid]:
                    start = mid
                else:
                    end = mid
        
        return answer

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
    
    def tearDown(self):
        pass

    def test_case_1(self):
        self.assertEqual( \
            self.solution.search([3], 3), \
            0)

    def test_case_2(self):
        self.assertEqual( \
            self.solution.search([1, 2, 3, 3, 4, 5, 10], 6), \
            -1)

    def test_case_3(self):
        self.assertEqual( \
            self.solution.search([1, 2, 3, 3, 4, 5, 10], 3), \
            2)

    def test_case_4(self):
        self.assertEqual( \
            self.solution.search([2,5], 5), \
            1)

if __name__ == '__main__':
    unittest.main()