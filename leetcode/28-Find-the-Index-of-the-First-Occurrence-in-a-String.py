class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack or len(haystack) < len(needle):
            return -1

        def match_word(word, target):
            if len(word) != len(target):
                return False

            for i, letter in enumerate(word):
                if letter != target[i]:
                    return False
            return True

        for i in range(len(haystack)):
            if match_word(
                    haystack[i:i+len(needle)],
                    needle
                ):
                return i
        return -1

