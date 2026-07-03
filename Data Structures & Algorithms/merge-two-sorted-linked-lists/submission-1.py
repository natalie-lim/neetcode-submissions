# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def helper(self, list1, list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        val1 = list1.val
        val2 = list2.val
        if val1 <= val2:
            list1.next = self.helper(list1.next, list2)
            return list1
        else: 
            list2.next = self.helper(list1, list2.next)
            return list2

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return self.helper(list1, list2)
        