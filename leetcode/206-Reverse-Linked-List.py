# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev_node = head
        node = head.next
        while node:
            next_node = node.next
            node.next = prev_node
            # step
            prev_node = node
            node = next_node
        head.next = None
        return prev_node
