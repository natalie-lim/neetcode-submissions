# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        pt1 = dummy
        pt2 = dummy
        for i in range(n):
            pt2 = pt2.next

        while pt2 is not None and pt2.next is not None:
            pt1 = pt1.next
            pt2 = pt2.next

        to_remove = pt1.next 
        to_connect = None
        if to_remove is not None:
            to_connect = pt1.next.next 
        pt1.next = to_connect

        if pt1 == dummy and pt1.next is None:
            return None
        elif pt1 == dummy:
            return pt1.next
        return head