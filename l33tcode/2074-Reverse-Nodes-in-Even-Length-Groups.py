# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return []

        to_reverse = []
        def get_group(node):
            i = 1
            group = []
            while node:
                group.append(node)
                if len(group) == i:
                    yield group
                    group = []
                    i += 1
                node = node.next
            if group:
                yield group

        def do_reverse(group):
            for i in range(len(group)-1, 0, -1):
                group[i].next = group[i-1]

        def reverse_group(group, start):
            do_reverse(group)
            start.next = group[-1]
            group[0].next = None
            return group[0]

        for group in get_group(head):
            to_reverse.append(group)

        start = end = None
        for group in to_reverse:
            if len(group) % 2:
                start = group[-1]
                # if we reversed group, we have an end as the last node to link to next group
                if end:
                    end.next = group[0]
                    # if last group is odd, prevent re-linking
                    end = None
            else:
                # if last group is even in length -> start would be the end of a last group
                start = end = reverse_group(group, start)
        return head
