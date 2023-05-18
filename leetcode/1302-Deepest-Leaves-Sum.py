from queue import deque
from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        stack = deque()
        level = 0
        stack.append((level, root))
        d = defaultdict(list)
        while stack:
            level, node = stack.popleft()
            d[level].append(node)
            level += 1
            for child in [node.left, node.right]:
                if child is not None:
                    stack.append((level, child))
        return sum([node.val for node in d[level-1]])
