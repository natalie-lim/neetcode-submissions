# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, p, q):
        if p != None and q != None and p.val != q.val:
            return False
        elif p == None and q != None:
            return False
        elif p != None and q == None:
            return False
        if p == None and q == None:
            return True
        right =  self.helper(p.right, q.right)
        left =  self.helper(p.left, q.left)
        return right and left

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.helper(p, q)