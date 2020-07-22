# https://leetcode.com/problems/clone-graph/

import unittest
from ...leetcode_data_model import Node


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node is None:
            return None

        # find all possible nodes
        original = set()
        original.add(node)
        self.findNode(original, node)

        # clone all possible nodes
        possibleNodes = dict()
        answer = Node(node.val)
        possibleNodes[answer.val] = answer

        for n in original:
            if n.val not in possibleNodes.keys():
                possibleNodes[n.val] = Node(n.val)

        # assign neighbors
        for n in original:

            tmp = possibleNodes[n.val]

            for neighbor in n.neighbors:
                tmp.neighbors.append(possibleNodes[neighbor.val])

        return answer

    def findNode(self, original, node):
        """
        :type original: set(Node)
        :node: Node
        """
        for n in node.neighbors:
            if n not in original:
                original.add(n)
                self.findNode(original, n)


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def test_case_1(self):
        node0 = Node(0)
        node1 = Node(1)
        node2 = Node(2)

        node0.neighbors.append(node1)
        node0.neighbors.append(node2)

        node1.neighbors.append(node2)

        node2.neighbors.append(node2)

        original = set()
        original.add(node0)
        self.solution.findNode(original, node0)

        answer = self.solution.cloneGraph(node0)
        answerSet = set()
        answerSet.add(answer)
        self.solution.findNode(answerSet, answer)

        self.assertEqual(len(original), len(answerSet))


if __name__ == '__main__':
    unittest.main()
