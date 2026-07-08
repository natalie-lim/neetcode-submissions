# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root, h):
        global b
        if root is None:
            return 0
        
        right_height = self.helper(root.right, h + 1)
        left_height = self.helper(root.left, h + 1)

        if not (right_height == left_height or (right_height + 1) == left_height or right_height == (left_height + 1)):
            b = False

        print ("right height: ", right_height, " left height: ", left_height)
        return 1 + max(right_height, left_height)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        global b
        b = True
        self.helper(root, 0)
        return b