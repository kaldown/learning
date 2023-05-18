# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = 0
        if not root:
            return result
        
        to_sum = []
        tmp_res = f"{root.val}"
        q = [(tmp_res, root)]

        while q:
            tmp_res, node = q.pop()
            
            if node.left is None and node.right is None:
                to_sum.append(int(tmp_res))

            for child in (node.left, node.right):
                if child is not None:
                    q.append((tmp_res+f"{child.val}", child))
                    
        return sum(to_sum)
