# https://leetcode.com/problems/merge-two-sorted-lists/

import unittest
from ...leetcode_data_model import ListNode

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        answer = None
        
        if l1 == None or l2 == None:
            
            if l1 == None:
                answer = l2
            elif l2 == None:
                answer = l1
            
        else:
        
            # copy first list
            answer = ListNode(l1.val)
            answerCurrent1 = answer
            
            current1 = l1
            while current1.next != None:
                answerCurrent1.next = ListNode(current1.next.val)
                answerCurrent1 = answerCurrent1.next
                current1 = current1.next

            current2 = l2
            while current2 != None:

                if answer.val > current2.val:
                    
                    toAdd = ListNode(current2.val)
                    toAdd.next = answer
                    answer = toAdd
                    
                else:
                    
                    inserted = False

                    answerCurrent2 = answer
                    while answerCurrent2.next != None:
                            
                        if answerCurrent2.next.val > current2.val:
                            
                            toAdd = ListNode(current2.val)
                            toAdd.next = answerCurrent2.next
                            answerCurrent2.next = toAdd
                            
                            inserted = True
                            break
                        
                        answerCurrent2 = answerCurrent2.next
                    
                    # add at tail
                    if inserted == False:
                        answerCurrent2.next = ListNode(current2.val)

                current2 = current2.next
                
        return answer
        
class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
    
    def tearDown(self):
        pass

    def test_case_1(self):
        
        list1 = ListNode(1)
        list1.next = ListNode(3)
        list1.next.next = ListNode(8)
        list1.next.next.next = ListNode(11)
        list1.next.next.next.next = ListNode(15)
        self.assertEqual(str(list1), "1->3->8->11->15")
        
        list2 = ListNode(2)
        self.assertEqual(str(list2), "2")
        
        self.assertEqual(str(self.solution.mergeTwoLists(list1, list2)), "1->2->3->8->11->15")

    def test_case_2(self):

        list1 = None
        
        list2 = ListNode(0)
        list2.next = ListNode(3)
        list2.next.next = ListNode(3)
        self.assertEqual(str(list2), "0->3->3")
        
        self.assertEqual(str(self.solution.mergeTwoLists(list1, list2)), "0->3->3")

if __name__ == '__main__':
    unittest.main()