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
        alr = {None: None} # og, newnode
        node = head
        # jus create copies of them all
        while node:
            copy = Node(node.val)
            alr[node] = copy
            node = node.next

        node = head
        while node:
            copy = alr[node]
            next_copy = alr[node.next]
            random_copy = alr[node.random]
            copy.next = next_copy
            copy.random = random_copy
            node = node.next
        
        return alr[head]