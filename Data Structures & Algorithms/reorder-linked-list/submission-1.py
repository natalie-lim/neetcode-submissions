# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head, prev):
        if head is None:
            return None
        if head.next is None:
            head.next = prev
            return head

        next_head = head.next
        head.next = prev
        return self.reverse(next_head, head)


    def reorderList(self, head: Optional[ListNode]) -> None:
        
        middle_pt = head
        pt2 = head

        while pt2.next is not None and pt2.next.next is not None:
            middle_pt = middle_pt.next
            pt2 = pt2.next.next

        head2 = middle_pt.next
        middle_pt.next = None

        # reverse the second half
        head2 = self.reverse(head2, None)

        idx = 1
        while head2 is not None:
            idx += 1
            head1next = head.next
            head.next = head2
            head = head2
            head2 = head1next

        