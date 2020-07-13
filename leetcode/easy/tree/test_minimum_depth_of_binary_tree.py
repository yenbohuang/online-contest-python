# https://leetcode.com/problems/minimum-depth-of-binary-tree/

import unittest
from ...leetcode_data_model import TreeNode


class Solution(object):

    __answer = 9999  # very big int

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        self.__findNode(root, 1)

        return self.__answer

    def __findNode(self, node, depth):
        """
        :type node: TreeNode
        :type depth: int
        :rtype: None
        """
        if node.left is None and node.right is None:

            if depth < self.__answer:
                self.__answer = depth

        if node.left is not None:
            self.__findNode(node.left, depth + 1)

        if node.right is not None:
            self.__findNode(node.right, depth + 1)


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

        self.assertEqual(self.solution.minDepth(root), 2)


if __name__ == '__main__':
    unittest.main()
