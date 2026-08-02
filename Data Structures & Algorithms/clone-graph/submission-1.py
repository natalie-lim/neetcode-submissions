"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        head = Node(node.val, None)

        def build(node, copy, d):
            # d is og : copy

            if len(node.neighbors) == 0:
                return

            neighbor_copies = []

            for n in node.neighbors:
                neighbor_copy = Node(n.val, None)
                if n not in d:
                    print("hi?")
                    neighbor_copies.append(neighbor_copy)
                    d[n] = neighbor_copy
                    build(n, neighbor_copy, d)
                else:
                    neighbor_copies.append(d[n])

            copy.neighbors = neighbor_copies

        build(node, head, {})
        return head
        
