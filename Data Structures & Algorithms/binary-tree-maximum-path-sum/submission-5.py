# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = float('-inf')

        # starts from the left or right
        def explore(node):
            nonlocal max_path

            if node.right is None and node.left is None:
                max_path = max(max_path, node.val)
                return node.val

            left = float('-inf')
            right = float('-inf')

            if node.left:
                left = explore(node.left)
            if node.right:
                right = explore(node.right)
            # include node and create bent path
            bent = node.val + max(0, left) + max(0, right)
            max_path = max(max_path, bent)
            path = max(0, left, right)
            return node.val + path

        return max(explore(root), max_path)