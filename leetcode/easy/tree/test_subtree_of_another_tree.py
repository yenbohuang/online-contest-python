#

import unittest
from ...leetcode_data_model import TreeNode


class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if t is None:
            return True
        elif s is None:
            return False
        else:
            return self.__compare(s, t) or \
                    (s.left is not None and self.isSubtree(s.left, t)) or \
                    (s.right is not None and self.isSubtree(s.right, t))

    def __compare(self, node1, node2):
        """
        :type node1: TreeNode
        :type node2: TreeNode
        :rtype: bool
        """
        if node1 is None and node2 is None:
            return True
        elif node1 is not None and node2 is not None \
                and node1.val == node2.val:
            return self.__compare(node1.left, node2.left) and \
                    self.__compare(node1.right, node2.right)
        else:
            return False


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def test_case_1(self):

        T1 = TreeNode(1)
        T1.left = TreeNode(2)
        T1.right = TreeNode(3)
        T1.right.left = TreeNode(4)

        T2 = TreeNode(3)
        T2.left = TreeNode(4)

        self.assertTrue(self.solution.isSubtree(T1, T2))

    def test_case_2(self):

        T1 = TreeNode(1)
        T1.left = TreeNode(2)
        T1.right = TreeNode(3)
        T1.right.left = TreeNode(4)

        T2 = TreeNode(3)
        T2.right = TreeNode(4)

        self.assertFalse(self.solution.isSubtree(T1, T2))

    def test_case_3(self):

        T1 = None

        T2 = TreeNode(3)
        T2.right = TreeNode(4)

        self.assertFalse(self.solution.isSubtree(T1, T2))

    def test_case_4(self):

        T1 = TreeNode(1)
        T1.left = TreeNode(2)
        T1.right = TreeNode(3)
        T1.right.left = TreeNode(4)

        T2 = None

        self.assertTrue(self.solution.isSubtree(T1, T2))

    def test_case_5(self):
        self.assertTrue(self.solution.isSubtree(None, None))


if __name__ == '__main__':
    unittest.main()
