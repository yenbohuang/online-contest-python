#

import unittest


class Solution(object):
    def testMethod(self, value):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return value


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def test_case_1(self):
        self.assertEqual(self.solution.testMethod(3), 3)


if __name__ == '__main__':
    unittest.main()
