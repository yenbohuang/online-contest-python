# https://leetcode.com/problems/reverse-linked-list/

import unittest
from ...leetcode_data_model import ListNode


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        root = ListNode(head.val)
        current = head.next

        while current is not None:

            node = ListNode(current.val)
            node.next = root
            root = node

            current = current.next

        return root


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def test_case_1(self):

        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)

        self.assertEqual(str(self.solution.reverseList(head)), "3->2->1")


if __name__ == '__main__':
    unittest.main()
