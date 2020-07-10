# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

import unittest
from ...leetcode_data_model import ListNode

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        
        current = head
        
        while current.next != None:
            
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        
        return head
        
class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
    
    def tearDown(self):
        pass

    def test_case_1(self):

        head = ListNode(1)
        head.next = ListNode(1)
        head.next.next = ListNode(2)
        
        self.assertEqual(str(self.solution.deleteDuplicates(head)), "1->2")

    def test_case_2(self):

        head = ListNode(1)
        head.next = ListNode(1)
        head.next.next = ListNode(2)
        head.next.next.next = ListNode(3)
        head.next.next.next.next = ListNode(3)
        
        self.assertEqual(str(self.solution.deleteDuplicates(head)), "1->2->3")

if __name__ == '__main__':
    unittest.main()