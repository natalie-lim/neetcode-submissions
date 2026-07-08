# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def helper(self, root, height):
        global max_di
        if root is None:
            return 0
      
        left_height = self.helper(root.left, height + 1)
        right_height = self.helper(root.right, height + 1)
        
        temp_sum = left_height + right_height
        if temp_sum > max_di:
            max_di = temp_sum

        return max(left_height, right_height) + 1


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global max_di
        max_di = 0
        self.helper(root, 0)
        return max_di