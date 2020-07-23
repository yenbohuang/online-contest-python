# https://leetcode.com/problems/insert-into-a-binary-search-tree/

import unittest
from ...leetcode_data_model import TreeNode


class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            return TreeNode(val)

        if root.val > val:

            if root.left is not None:
                self.insertIntoBST(root.left, val)
            else:
                root.left = TreeNode(val)

        else:

            if root.right is not None:
                self.insertIntoBST(root.right, val)
            else:
                root.right = TreeNode(val)

        return root


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def test_case_1(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.right.left = TreeNode(3)

        answer = self.solution.insertIntoBST(root, 6)

        self.assertEqual(2, answer.val)

        self.assertEqual(1, answer.left.val)
        self.assertIsNone(answer.left.left)
        self.assertIsNone(answer.left.right)

        self.assertEqual(4, answer.right.val)

        self.assertEqual(3, answer.right.left.val)
        self.assertIsNone(answer.right.left.left)
        self.assertIsNone(answer.right.left.right)

        self.assertEqual(6, answer.right.right.val)
        self.assertIsNone(answer.right.right.left)
        self.assertIsNone(answer.right.right.right)


if __name__ == '__main__':
    unittest.main()
