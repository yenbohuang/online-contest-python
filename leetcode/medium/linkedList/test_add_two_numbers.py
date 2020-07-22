# https://leetcode.com/problems/add-two-numbers/

import unittest
from ...leetcode_data_model import ListNode


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        answer = ListNode(0)

        cursor1 = l1
        cursor2 = l2
        cursorAnswer = answer

        tmp = 0

        while cursor1 is not None or cursor2 is not None:

            if cursor1 is not None:
                tmp += cursor1.val
                cursor1 = cursor1.next

            if cursor2 is not None:
                tmp += cursor2.val
                cursor2 = cursor2.next

            cursorAnswer.val = tmp % 10
            tmp //= 10

            if tmp > 0 or cursor1 is not None or cursor2 is not None:
                newNode = ListNode(tmp)
                cursorAnswer.next = newNode
                cursorAnswer = newNode

        return answer


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def test_case_1(self):
        caseA1_1 = ListNode(7)
        caseA1_2 = ListNode(1)
        caseA1_1.next = caseA1_2
        caseA1_3 = ListNode(6)
        caseA1_2.next = caseA1_3

        caseA2_1 = ListNode(5)
        caseA2_2 = ListNode(9)
        caseA2_1.next = caseA2_2
        caseA2_3 = ListNode(2)
        caseA2_2.next = caseA2_3

        self.assertEqual(str(caseA1_1), "7->1->6")
        self.assertEqual(str(caseA2_1), "5->9->2")
        self.assertEqual(
            str(self.solution.addTwoNumbers(caseA1_1, caseA2_1)), "2->1->9")

    def test_case_2(self):
        caseB1_1 = ListNode(3)
        caseB1_2 = ListNode(1)
        caseB1_1.next = caseB1_2
        caseB1_3 = ListNode(5)
        caseB1_2.next = caseB1_3

        caseB2_1 = ListNode(5)
        caseB2_2 = ListNode(9)
        caseB2_1.next = caseB2_2
        caseB2_3 = ListNode(2)
        caseB2_2.next = caseB2_3

        self.assertEqual(str(caseB1_1), "3->1->5")
        self.assertEqual(str(caseB2_1), "5->9->2")
        self.assertEqual(str(self.solution.addTwoNumbers(caseB1_1, caseB2_1)),
                         "8->0->8")


if __name__ == '__main__':
    unittest.main()
