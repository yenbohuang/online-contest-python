# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

import unittest
from ...leetcode_data_model import ListNode


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        current = head
        count = 0

        while current is not None:
            count += 1
            current = current.next

        if count == 1 and n == 1:
            return None
        elif count - n == 0:
            return head.next

        current = head

        for i in range(count):

            if i == count - n - 1:
                current.next = current.next.next
                break

            current = current.next

        return head


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def test_case_1(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)

        self.assertEqual(
            str(self.solution.removeNthFromEnd(head, 2)), "1->2->3->5")

    def test_case_2(self):
        self.assertIsNone(self.solution.removeNthFromEnd(ListNode(1), 1))

    def test_case_3(self):
        head = ListNode(1)
        head.next = ListNode(2)

        self.assertEqual(str(self.solution.removeNthFromEnd(head, 2)), "2")


if __name__ == '__main__':
    unittest.main()
