# Use relative import: https://docs.python.org/2.5/whatsnew/pep-328.html
# for example: "from ...leetcode_data_model import ListNode" in "leetcode.easy.linkedList.*"

class ListNode(object):
    def __init__(self, x):

        self.val = x
        self.next = None
    
    def __str__(self):

        cursor = self
        value = str(self.val)
        
        while cursor.next != None:
            value += "->" + str(cursor.next.val)
            cursor = cursor.next
        
        return value
