# https://leetcode.com/problems/merge-sorted-array/

import unittest


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for i in range(0, n):

            inserted = False

            for j in range(0, m):

                if nums1[j] > nums2[i]:
                    self.shift(nums1, m, j)
                    nums1[j] = nums2[i]
                    m += 1
                    inserted = True
                    break

            if False is inserted:
                nums1[m] = nums2[i]
                m += 1

    def shift(self, nums, size, start):

        for i in range(size, start, -1):
            nums[i] = nums[i - 1]


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def test_shift_function(self):
        nums1 = [1, 2, 3, 0, 0]
        self.solution.shift(nums1, 3, 0)
        self.assertEqual(nums1, [1, 1, 2, 3, 0])

    def test_case_1(self):

        nums1 = [1, 2, 3, 0, 0]
        self.solution.merge(nums1, 3, [4, 5], 2)
        self.assertEqual(nums1, [1, 2, 3, 4, 5])

    def test_case_2(self):

        nums1 = [1, 2, 3, 0, 0]
        self.solution.merge(nums1, 3, [4, 5], 2)
        self.assertEqual(nums1, [1, 2, 3, 4, 5])

    def test_case_3(self):

        nums1 = [1, 2, 3, 0, 0]
        self.solution.merge(nums1, 3, [4, 5], 2)
        self.assertEqual(nums1, [1, 2, 3, 4, 5])

    def test_case_4(self):

        nums1 = [1, 2, 3, 0, 0]
        self.solution.merge(nums1, 3, [4, 5], 2)
        self.assertEqual(nums1, [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
