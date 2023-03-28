# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers_recursion(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node: TreeNode, past_num: str) -> int:
            if node:
                if not node.left and not node.right:
                    return int(past_num+str(node.val))
                return dfs(node.left, past_num+str(node.val)) + dfs(node.right, past_num+str(node.val))
            return 0
        return dfs(root, "0")

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        summa = 0
        stack = deque([(root, "0")])
        while stack:
            node, digit = stack.pop()
            if node:
                if not node.left and not node.right:
                    summa += int(digit + str(node.val))
                stack.append([node.left, digit + str(node.val)])
                stack.append([node.right, digit + str(node.val)])
        return summa

