# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        l = [(root, 1)]

        while l:
            node, level = l.pop(0)
            if node:
                if not node.left and not node.right:
                    return level
                l.append((node.left, level+1))
                l.append((node.right, level+1))
