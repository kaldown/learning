"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        def print_pre(node):
            if node:
                result.append(node.val)
                
                for child in node.children:
                    print_pre(child)
        print_pre(root)
        return result
