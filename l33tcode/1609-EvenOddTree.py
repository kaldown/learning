from collections import defaultdict
from queue import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:

        def check_odd(number, is_odd):
            res = number % 2
            if is_odd:
                if res:
                    return False
            else:
                if not res:
                    return False
            return True
        
        def check_level(level):
            arr = d[level]

            is_odd = bool(level % 2)
            forward_direction = False if is_odd else True
            arr = arr if forward_direction else list(reversed(arr)) 

            prev_num = arr[0]
            
            if not check_odd(prev_num, is_odd):

                return False
            
            for number in arr[1:]:

                if not number > prev_num:
                    return False
                if not check_odd(number, is_odd):
                    return False
                prev_num = number
            
            return True
        
        d = defaultdict(list)
        level = 0
        
        stack = deque()
        stack.append((level, root))
        
        prev_level = level
        while stack:
            level, node = stack.popleft()
            d[level].append(node.val)
            if level > prev_level:
                if not check_level(prev_level):
                    return False
                
            for child in (node.left, node.right):
                if child is not None:
                    stack.append((level+1, child))
            prev_level = level
        
        return check_level(level)
