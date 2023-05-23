class Solution:
    def isValid(self, s: str) -> bool:
        open_par = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        stack = []
        for par in s:
            if par in open_par:
                stack.append(open_par[par])
            else:
                close_par = stack.pop() if stack else None
                if close_par != par:
                    return False
        if stack:
            return False
        return True

