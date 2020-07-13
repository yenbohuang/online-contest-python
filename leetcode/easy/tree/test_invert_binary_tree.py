# https://leetcode.com/problems/invert-binary-tree/

import unittest
from ...leetcode_data_model import TreeNode


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None

        tmp = root.left
        root.left = root.right
        root.right = tmp

        if root.left is not None:
            self.invertTree(root.left)

        if root.right is not None:
            self.invertTree(root.right)

        return root


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

        self.solution.invertTree(root)

        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 3)
        self.assertEqual(root.left.right.val, 4)
        self.assertEqual(root.right.val, 2)


if __name__ == '__main__':
    unittest.main()
