# https://leetcode.com/problems/binary-tree-postorder-traversal/

import unittest
from ...leetcode_data_model import TreeNode


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        target = list()

        if root is not None:
            self.__traverse(root, target)

        return target

    def __traverse(self, node,  target):
        """
        :type node: TreeNode
        :type target: List[int]
        :rtype: None
        """
        if node.left is not None:
            self.__traverse(node.left, target)

        if node.right is not None:
            self.__traverse(node.right, target)

        target.append(node.val)


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def test_case_1(self):

        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)

        self.assertEqual(self.solution.postorderTraversal(root), [3, 2, 1])


if __name__ == '__main__':
    unittest.main()
