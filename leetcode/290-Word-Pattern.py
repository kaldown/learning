class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        s = s.split()
        if len(pattern) != len(s):
            return False

        for i, letter in enumerate(pattern):
            if letter in d:
                d[letter].append(i)
            else:
                d[letter] = [i]
        uniques = set()
        shift = 0
        for indexes in d.values():
            shift += 1
            for i in indexes:
                uniques.add(s[i])
                if not len(uniques) == shift:
                    return False
        return True
