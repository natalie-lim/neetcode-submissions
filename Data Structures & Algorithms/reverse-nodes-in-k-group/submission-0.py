# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverse(node, prev):
            if node == None:
                return prev
            next_node = node.next
            node.next = prev
            return reverse(next_node, node)

        found_head = False
        new_head = None
        curr = head
        
        def helper(n, prev):
            nonlocal found_head
            nonlocal new_head
            less_than_k = False
            if n is None:
                return None
            start = n
            for i in range(k-1):
                if n.next == None:
                    less_than_k = True
                    break
                n = n.next
            
            if less_than_k:
                return start
                
            print("starting on: ", n.val)
            next_start = n.next
            n.next = None
            prev = reverse(start, None)
            print("ok prev: ", prev.val)
            if not found_head:
                new_head = prev
                found_head = True
            print("tail: ", start.val)
            start.next = helper(next_start, prev)
            return prev

        
        helper(head, None)
        print("new head: ", new_head.val)
        return new_head