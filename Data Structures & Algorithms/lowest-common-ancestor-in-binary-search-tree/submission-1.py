# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pfound = False
        qfound = False
        
        while not pfound and not qfound:
            val = root.val
            if root.val == p.val:
                pfound = True
            if root.val == q.val:
                qfound = True

            if p.val < val and q.val < val:
                root = root.left
            elif p.val > val and q.val > val:
                root = root.right
            else:
                return root

        return root