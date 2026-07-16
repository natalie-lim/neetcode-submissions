# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def helper(self, root, max_val, min_val):
        if root is None:
            return True
        right = root.right
        left = root.left

        if left is not None and (left.val >= root.val or left.val <= min_val):
            return False
        if right is not None and (right.val <= root.val or right.val >= max_val):
            return False
        
        return self.helper(root.left, root.val, min_val) and self.helper(root.right, max_val, root.val)
        
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, (float('inf')), (float('-inf')))