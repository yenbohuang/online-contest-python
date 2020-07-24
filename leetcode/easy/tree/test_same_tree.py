# https://leetcode.com/problems/same-tree/

import unittest
from ...leetcode_data_model import TreeNode


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        elif p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) \
            and self.isSameTree(p.right, q.right)


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def test_case_1(self):

        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(3)

        q = TreeNode(1)
        q.left = TreeNode(2)
        q.right = TreeNode(3)

        self.assertTrue(self.solution.isSameTree(p, q))

    def test_case_2(self):

        p = TreeNode(1)
        p.left = TreeNode(2)

        q = TreeNode(1)
        q.right = TreeNode(2)

        self.assertFalse(self.solution.isSameTree(p, q))

    def test_case_3(self):

        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(1)

        q = TreeNode(1)
        q.left = TreeNode(1)
        q.right = TreeNode(2)

        self.assertFalse(self.solution.isSameTree(p, q))


if __name__ == '__main__':
    unittest.main()
