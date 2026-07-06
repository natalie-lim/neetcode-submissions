# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        d = {}
        idx = 0
        if head == None:
            return False
        while head.next != None:
            if head in d:
                return True
            
            d[head] = idx
            idx += 1
            head = head.next

        return False