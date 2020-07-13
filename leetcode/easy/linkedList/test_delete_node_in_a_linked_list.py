# https://leetcode.com/problems/delete-node-in-a-linked-list/

import unittest
from ...leetcode_data_model import ListNode


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def test_case_1(self):

        root = ListNode(1)
        root.next = ListNode(2)
        root.next.next = ListNode(3)
        root.next.next.next = ListNode(4)

        self.assertEqual(str(root), "1->2->3->4")

        self.solution.deleteNode(root.next.next)
        self.assertEqual(str(root), "1->2->4")


if __name__ == '__main__':
    unittest.main()
