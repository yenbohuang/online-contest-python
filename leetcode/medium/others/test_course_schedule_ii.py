# https://leetcode.com/problems/course-schedule-ii/
# http://en.wikipedia.org/wiki/Topological_sorting#Algorithms

import unittest


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if prerequisites is None:
            return list()

        if not prerequisites:
            if numCourses > 0:
                return list(range(numCourses))
            else:
                return list()

        possibleCourseSet = set(range(numCourses))
        numOfEdges = len(prerequisites)

        # Empty list that will contain the sorted elements
        sortedArrayList = [0] * numCourses
        sortedArrayIndex = 0

        # Set of all nodes with no incoming edges
        noIncomingEdgeSet = set()
        hasIncomingEdgesList = [0] * numCourses

        for i in prerequisites:

            hasIncomingEdgesList[i[0]] = hasIncomingEdgesList[i[0]] + 1
            noIncomingEdgeSet.discard(i[0])

            if hasIncomingEdgesList[i[1]] > 0:
                noIncomingEdgeSet.discard(i[1])
            else:
                noIncomingEdgeSet.add(i[1])

        while noIncomingEdgeSet:

            n = noIncomingEdgeSet.pop()
            sortedArrayList[sortedArrayIndex] = n
            possibleCourseSet.discard(n)
            sortedArrayIndex += 1
            noIncomingEdgeSet.discard(n)

            for i in prerequisites:

                if i[0] != -1:

                    m = i[0]

                    if i[1] == n:

                        hasIncomingEdgesList[m] = hasIncomingEdgesList[m] - 1
                        i[0] = -1
                        i[1] = -1
                        numOfEdges -= 1

                    if hasIncomingEdgesList[m] == 0:
                        noIncomingEdgeSet.add(m)

        if numOfEdges == 0:

            if possibleCourseSet:

                for n in possibleCourseSet:
                    sortedArrayList[sortedArrayIndex] = n
                    sortedArrayIndex += 1

            return sortedArrayList
        else:
            return list()


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def test_case_1(self):
        self.assertEqual(self.solution.findOrder(2, [[1, 0]]), [0, 1])

    def test_case_2(self):
        self.assertEqual(
            self.solution.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]),
            [0, 1, 2, 3])


if __name__ == '__main__':
    unittest.main()
