# https://leetcode.com/problems/binary-tree-inorder-traversal/

import unittest
from ...leetcode_data_model import TreeNode


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        answer = list()

        if root is not None:
            self.traverse(root, answer)

        return answer

    def traverse(self, node, answer):
        """
        :type node: TreeNode
        :type answer: List[int]
        """
        if node.left is not None:
            self.traverse(node.left, answer)

        answer.append(node.val)

        if node.right is not None:
            self.traverse(node.right, answer)


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def test_case_1(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)

        self.assertEqual(self.solution.inorderTraversal(root), [1, 3, 2])


if __name__ == '__main__':
    unittest.main()
