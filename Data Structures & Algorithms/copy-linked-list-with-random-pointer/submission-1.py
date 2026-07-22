"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d = {}
        node = head

        while node is not None:
            val = node.val

            new_node = Node(val, None, None)
            d[node] = new_node
            node = node.next
        
        for og, new_node in d.items():
            print(og.val)
            next_node = og.next
            random_node = og.random
            new_node.next = d[next_node] if next_node else None
            new_node.random = d[random_node] if random_node else None
        
        if head is None:
            return None
        return d[head]