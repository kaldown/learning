class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = {}
        for letter in s:
            if letter in d:
                d[letter] += 1
            else:
                d[letter] = 1

        return True if len(set(d.values())) == 1 else False
