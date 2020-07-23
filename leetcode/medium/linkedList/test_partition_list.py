# https://leetcode.com/problems/partition-list/

import unittest
from ...leetcode_data_model import ListNode


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        greaterThan = list()
        lessThan = list()
        node = head

        while node is not None:

            if node.val < x:
                lessThan.append(node.val)
            else:
                greaterThan.append(node.val)

            node = node.next

        lessThan.extend(greaterThan)

        answer = ListNode(lessThan[0])
        tmpNode = answer

        for i in range(1, len(lessThan)):
            tmpNode.next = ListNode(lessThan[i])
            tmpNode = tmpNode.next

        return answer


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def test_case_1(self):
        # 1->4->3->2->5->2
        head = ListNode(1)
        head.next = ListNode(4)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(2)
        head.next.next.next.next = ListNode(5)
        head.next.next.next.next.next = ListNode(2)

        self.assertEqual(
            str(self.solution.partition(head, 3)), "1->2->2->4->3->5")

    def test_case_2(self):
        self.assertIsNone(self.solution.partition(None, 3))


if __name__ == '__main__':
    unittest.main()
