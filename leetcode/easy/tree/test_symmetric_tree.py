# https://leetcode.com/problems/symmetric-tree/

import unittest
from ...leetcode_data_model import TreeNode


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        return self.__match(root, root)

    def __match(self, nodeLeft, nodeRight):

        if nodeLeft is None and nodeRight is None:
            return True
        elif nodeLeft is not None and nodeRight is not None:
            return nodeLeft.val == nodeRight.val \
                and self.__match(nodeLeft.left, nodeRight.right) \
                and self.__match(nodeLeft.right, nodeRight.left)
        else:
            return False


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def test_case_1(self):

        root = TreeNode(1)

        root.left = TreeNode(2)
        root.right = TreeNode(2)

        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(3)

        self.assertTrue(self.solution.isSymmetric(root))

    def test_case_2(self):

        root = TreeNode(1)

        root.left = TreeNode(2)
        root.right = TreeNode(2)

        root.left.right = TreeNode(3)
        root.right.right = TreeNode(3)

        self.assertFalse(self.solution.isSymmetric(root))


if __name__ == '__main__':
    unittest.main()
