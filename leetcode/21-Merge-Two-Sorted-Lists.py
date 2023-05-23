# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        result = []
        left = list1
        right = list2
        while left and right:
            if left.val <= right.val:
                result.append(left)
                left = left.next
            else:
                result.append(right)
                right = right.next
        
        while left:
            result.append(left)
            left = left.next

        while right:
            result.append(right)
            right = right.next

        
        for i in range(len(result) - 1):
            result[i].next = result[i+1]
        result[-1].next = None

        return result[0]

