# https://leetcode.com/problems/balanced-binary-tree/

import unittest
from ...leetcode_data_model import TreeNode


class Solution(object):

    __balanced = True

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        self.__findNode(root, 1)

        return self.__balanced

    def __findNode(self, node, depth):
        """
        :type node: TreeNode
        :type depth: int
        :rtype: int
        """

        if node.left is None and node.right is None:
            return depth

        leftDepth = depth
        rightDepth = depth

        if node.left is not None:
            leftDepth = self.__findNode(node.left, depth + 1)

        if node.right is not None:
            rightDepth = self.__findNode(node.right, depth + 1)

        if abs(rightDepth - leftDepth) > 1:
            self.__balanced = False

        return max(rightDepth, leftDepth)


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def test_case_1(self):

        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        self.assertTrue(self.solution.isBalanced(root))

    def test_case_2(self):

        root = TreeNode(3)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        self.assertFalse(self.solution.isBalanced(root))

    def test_case_3(self):
        self.assertTrue(self.solution.isBalanced(None))

    def test_case_4(self):

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        root.left.left.left = TreeNode(8)
        root.left.left.right = TreeNode(9)
        root.left.right.left = TreeNode(10)
        root.left.right.right = TreeNode(11)
        root.right.left.left = TreeNode(12)
        root.right.left.right = TreeNode(13)
        root.right.right.left = TreeNode(14)
        root.right.right.right = TreeNode(15)
        root.left.left.left.left = TreeNode(16)

        self.assertTrue(self.solution.isBalanced(root))


if __name__ == '__main__':
    unittest.main()
