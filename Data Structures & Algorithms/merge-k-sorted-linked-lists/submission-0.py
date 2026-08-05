# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        ListNode.__lt__ = lambda self, other: self.val < other.val
        current_min = float('inf')
        heap = []
        for n in lists:
            if n is not None:
                current_min = n.val
                heapq.heappush(heap, n)

        head = heapq.heappop(heap)
        to_push = head.next
        if to_push is not None:
            heapq.heappush(heap, head.next)
        curr = head

        while heap:
            popped = heapq.heappop(heap)
            curr.next = popped
            curr = popped
            if curr.next != None:
                heapq.heappush(heap, curr.next)
        
        return head
        