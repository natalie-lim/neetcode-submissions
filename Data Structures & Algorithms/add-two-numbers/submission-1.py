# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l = None
        head = None
        ones = 0

        while l1 is not None or l2 is not None:
            val1 = 0
            val2 = 0

            if l1 is not None:
                val1 = l1.val
            if l2 is not None:
                val2 = l2.val

            added = val1 + val2 + ones
            r = added % 10
            ones = added // 10
            print(added)

            if l is not None:
                l.next = ListNode(r)
                l = l.next
            else:
                l = ListNode(r)
                head = l

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        if ones != 0:
            l.next = ListNode(ones)

        return head

