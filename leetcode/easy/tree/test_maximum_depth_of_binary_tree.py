# https://leetcode.com/problems/maximum-depth-of-binary-tree/

import unittest
from ...leetcode_data_model import TreeNode


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        return self.__findNode(root, 1)

    def __findNode(self, node,  depth):
        """
        :type node: TreeNode
        :type depth: int
        :rtype: int
        """
        if node.left is None and node.right is None:
            return depth

        leftDepth = -1
        rightDepth = -1

        if node.left is not None:
            leftDepth = self.__findNode(node.left, depth + 1)

        if node.right is not None:
            rightDepth = self.__findNode(node.right, depth + 1)

        if rightDepth > leftDepth:
            return rightDepth
        else:
            return leftDepth


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def test_case_1(self):

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(5)

        self.assertEqual(self.solution.maxDepth(root), 3)


if __name__ == '__main__':
    unittest.main()
