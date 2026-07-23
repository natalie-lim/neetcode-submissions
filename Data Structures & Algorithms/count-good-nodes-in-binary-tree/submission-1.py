# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper (self, node, max_val):
        if node is None:
            return 0
        val = node.val
        add = 0
        if val >= max_val:
            add = 1
            max_val = val
        return add + self.helper(node.right, max_val) + self.helper(node.left, max_val)

        

    def goodNodes(self, root: TreeNode) -> int:
        return self.helper(root, float('-inf'))