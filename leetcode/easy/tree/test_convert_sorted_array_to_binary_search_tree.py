# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

import unittest
from ...leetcode_data_model import TreeNode

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums == None or len(nums) == 0:
            return None
        
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        
        self.__construct(root, nums, 0, mid - 1, True)
        self.__construct(root, nums, mid + 1, len(nums) - 1, False)
        
        return root

    def __construct(self, node, nums, start, end, left):
        """
        :type node: TreeNode
        :type nums: List[int]
        :type start: int
        :type end: int
        :type left: boolean
        :rtype: None
        """
        if end < start:
            return
        
        mid = start + ((end - start) // 2)
        newNode = TreeNode(nums[mid])
        
        if left:
            node.left = newNode
        else:
            node.right = newNode
        
        self.__construct(newNode, nums, start, mid - 1, True)
        self.__construct(newNode, nums, mid + 1, end, False)
        
class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
    
    def tearDown(self):
        pass

    def test_case_1(self):

        root = self.solution.sortedArrayToBST([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(root.val, 4)
        
        self.assertEqual(root.left.val, 2)
        self.assertEqual(root.left.left.val, 1)
        self.assertEqual(root.left.right.val, 3)
        
        self.assertEqual(root.right.val, 6)
        self.assertEqual(root.right.left.val, 5)
        self.assertEqual(root.right.right.val, 7)

    def test_case_2(self):
        self.assertIsNone(self.solution.sortedArrayToBST(None))
    
    def test_case_3(self):
        self.assertIsNone(self.solution.sortedArrayToBST(list()))
    
    def test_case_4(self):
        
        root = self.solution.sortedArrayToBST([-10,-3,0,5,9])
        self.assertEqual(root.val, 0)
        
        self.assertEqual(root.left.val, -10)
        self.assertEqual(root.left.right.val, -3)
        
        self.assertEqual(root.right.val, 5)
        self.assertEqual(root.right.right.val, 9)

if __name__ == '__main__':
    unittest.main()