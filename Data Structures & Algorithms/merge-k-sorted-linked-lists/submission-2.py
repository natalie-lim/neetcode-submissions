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
        heap = lists
        heapq.heapify(heap)

        head = heapq.heappop(heap)
        curr = head
        if head.next is not None:
            heapq.heappush(heap, head.next)

        while heap:
            add = heapq.heappop(heap)
            curr.next = add
            if add.next is not None:
                heapq.heappush(heap, add.next)
            curr = add
        
        return head
