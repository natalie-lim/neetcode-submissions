# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def matchTree (self, root, subRoot):
        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None:
            return False
        if root.val != subRoot.val:
            return False
        
        return self.matchTree(root.right, subRoot.right) and self.matchTree(root.left, subRoot.left)

    def findStart (self, root, subRoot):
        if root is None:
            return False

        if root.val == subRoot.val and self.matchTree(root, subRoot):
            return True

        return self.findStart(root.right, subRoot) or self.findStart(root.left, subRoot)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.findStart(root, subRoot)