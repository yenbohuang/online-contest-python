# https://leetcode.com/problems/binary-tree-preorder-traversal/

import unittest
from ...leetcode_data_model import TreeNode


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        answer = list()

        if root is not None:
            self.traverse(root, answer)

        return answer

    def traverse(self, node, answer):

        answer.append(node.val)

        if node.left is not None:
            self.traverse(node.left, answer)

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

        self.assertEqual(self.solution.preorderTraversal(root), [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
