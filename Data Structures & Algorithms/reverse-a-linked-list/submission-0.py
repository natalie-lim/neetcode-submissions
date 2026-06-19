# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def helper(self, prev, curr_node):
        if curr_node.next == None:
            curr_node.next = prev
            return curr_node

        next_node = curr_node.next
        curr_node.next = prev

        print ("next: ", next_node.val)
        print("curr: ", curr_node.val)

        return self.helper(curr_node, next_node)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        return self.helper(None, head)
        