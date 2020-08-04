# https://leetcode.com/problems/path-sum/

import unittest
from ...leetcode_data_model import TreeNode


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.__traverse(root, 0, sum)

    def __traverse(self, node, prevSum, sum):
        """
        :type node: TreeNode
        :type prevSum: int
        :type sum: int
        :rtype: bool
        """
        if node is None:
            return False

        if node.left is None and node.right is None:
            # leaf
            return (prevSum + node.val == sum)
        else:
            return self.__traverse(node.left, prevSum + node.val, sum) \
                or self.__traverse(node.right, prevSum + node.val, sum)


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def test_case_1(self):
        root = TreeNode(5)

        root.left = TreeNode(4)
        root.right = TreeNode(8)

        root.left.left = TreeNode(11)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)

        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)
        root.right.right.right = TreeNode(1)

        self.assertTrue(self.solution.hasPathSum(root, 22))


if __name__ == '__main__':
    unittest.main()
