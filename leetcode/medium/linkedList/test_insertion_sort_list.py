# https://leetcode.com/problems/insertion-sort-list/

import unittest
from ...leetcode_data_model import ListNode


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        if head.next is None:
            return head

        newRoot = ListNode(head.val)
        srcNode = head.next

        while srcNode is not None:

            node = newRoot

            while node.val < srcNode.val and node.next is not None:
                node = node.next

            addNode = None

            if node.val < srcNode.val:
                addNode = ListNode(srcNode.val)
            else:
                addNode = ListNode(node.val)
                node.val = srcNode.val

            addNode.next = node.next
            node.next = addNode
            srcNode = srcNode.next

        return newRoot


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def test_case_1(self):
        root = ListNode(1)

        self.assertEqual(str(root), "1")
        self.assertEqual(str(self.solution.insertionSortList(root)), "1")

    def test_case_2(self):
        root = ListNode(1)
        root.next = ListNode(3)
        root.next.next = ListNode(2)
        root.next.next.next = ListNode(0)

        self.assertEqual(str(root), "1->3->2->0")
        self.assertEqual(
            str(self.solution.insertionSortList(root)), "0->1->2->3")

    def test_case_3(self):
        self.assertIsNone(self.solution.insertionSortList(None))


if __name__ == '__main__':
    unittest.main()
