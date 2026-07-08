# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper (self, root, l):
        if root == None:
            return l
        
        return max(self.helper(root.left, (l + 1)), self.helper(root.right, (l + 1)))


    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.helper(root, 0)