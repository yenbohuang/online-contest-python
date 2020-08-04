# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

from leetcode.leetcode_data_model import TreeNode
import unittest


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        answer = list(list())

        if root is None:
            return answer

        self.__traverse(root, answer, 1)
        answer.reverse()
        return answer

    def __traverse(self, node, answer, level):
        """
        :type node: TreeNode
        :answer: List[List[int]]
        :level: int
        """
        if node is None:
            return

        if len(answer) < level:
            answer.append(list())

        answer[level - 1].append(node.val)
        self.__traverse(node.left, answer, level + 1)
        self.__traverse(node.right, answer, level + 1)


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

        self.assertEqual(self.solution.levelOrderBottom(root),
                         [[15, 7], [9, 20], [3]])


if __name__ == '__main__':
    unittest.main()
