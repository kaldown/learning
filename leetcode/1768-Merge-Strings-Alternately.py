class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        for i in range(min(len(word1), len(word2))):
            left = word1[i]
            right = word2[i]
            result.extend([left, right])
        result.extend(word1[i+1:])
        result.extend(word2[i+1:])
        return ''.join(result)

