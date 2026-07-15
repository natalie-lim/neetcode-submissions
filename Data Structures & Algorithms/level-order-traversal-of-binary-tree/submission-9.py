# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            l = len(q)
            
            level = []
            for i in range(l):
                node = q.pop()
                level.append(node.val)
                if node.left is not None:
                    q.appendleft(node.left)
                if node.right is not None:
                    q.appendleft(node.right)
            
            res.append(level)

        return res

