# Use relative import: https://docs.python.org/2.5/whatsnew/pep-328.html
# for example:
# "from ...leetcode_data_model import ListNode" in "leetcode.easy.linkedList.*"

# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):

        self.val = x
        self.next = None

    def __str__(self):

        cursor = self
        value = str(self.val)

        while cursor.next is not None:
            value += "->" + str(cursor.next.val)
            cursor = cursor.next

        return value


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for a graph node.
class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
