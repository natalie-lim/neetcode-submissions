# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""

        q = deque()
        q.append(root)
        s = ""

        while q:
            node = q.pop()
            if node is not None:
                s += str(node.val) + ","
                right = node.right
                left = node.left
                q.appendleft(left)
                q.appendleft(right)
            else:
                s += "$,"

        print(s)
        return s

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data) == 0:
            return None

        arr = []
        acc = ""
        for c in data:
            if c == ",":
                if acc == "$":
                    arr.append(None)
                else:
                    arr.append(int(acc))
                acc = ""
            else:
                acc += (c)

        head = TreeNode(arr[0], None, None)
        q = deque()
        q.append(head)

        for idx, n in enumerate(arr[1:]):
            if q:
                curr = q.pop()
                if idx % 2 == 0:
                    # left
                    if n:
                        curr.left = TreeNode(n, None, None)
                        if curr.left:
                            q.appendleft(curr.left)
                    q.append(curr)
                else:
                    # right
                    if n:
                        curr.right = TreeNode(n, None, None)
                        q.appendleft(curr.right)

        return head
        
