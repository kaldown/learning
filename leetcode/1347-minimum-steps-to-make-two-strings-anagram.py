class Solution:
    def minSteps(self, s: str, t: str) -> int:
        d = {}
        for l in s:
            if l in d:
                d[l] += 1
            else:
                d[l] = 1
                
        leftovers = []
        for l in t:
            if l in d:
                d[l] -= 1
                if d[l] == 0:
                    del d[l]
            else:
                leftovers.append(l)
        return len(leftovers)
