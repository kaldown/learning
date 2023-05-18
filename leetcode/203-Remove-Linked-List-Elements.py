# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head or not head.val:
            return head

        node = head
        while node:
            fast_node = node.next
            if fast_node and fast_node.val == val:
                node.next = fast_node.next
            else:
                node = node.next

        if head.val == val:
            head = head.next

        return head
