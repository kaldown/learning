from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        result = [[]]
        q = deque([[root, 0]])
        while q:
            node, level = q.popleft()
            if len(result) < level + 1:
                result.append([])
            result[level].append(node.val)
            for child in node.children:
                q.append([child, level + 1])
        return result
