# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        q = deque()
        q.append(root)
        l = []

        while q:
            len_q = len(q)
            for i in range(len_q):
                node = q.pop()
                if i == 0:
                    l.append(node.val)
                
                if node.right is not None:
                    q.appendleft(node.right)
                if node.left is not None:
                    q.appendleft(node.left)

        return l