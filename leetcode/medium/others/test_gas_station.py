# https://leetcode.com/problems/gas-station/

import unittest


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        gasSize = len(gas)

        for i in range(gasSize):

            inTank = 0

            for j in range(gasSize):

                index = (i + j) % gasSize
                inTank += (gas[index] - cost[index])

                if inTank < 0:
                    break

            if inTank >= 0:
                return i

        return -1


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def test_case_1(self):
        self.assertEqual(
            self.solution.canCompleteCircuit([1, 1, 3, 1], [2, 2, 1, 1]), 2)

    def test_case_2(self):
        self.assertEqual(
            self.solution.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]),
            3)

    def test_case_3(self):
        self.assertEqual(
            self.solution.canCompleteCircuit([2, 3, 4], [3, 4, 3]), -1)


if __name__ == '__main__':
    unittest.main()
