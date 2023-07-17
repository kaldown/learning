class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        stack = [l for l in reversed(s)]
        for letter in t:
            if not stack:
                return True
            if stack[-1] == letter:
                stack.pop()
        return not stack

