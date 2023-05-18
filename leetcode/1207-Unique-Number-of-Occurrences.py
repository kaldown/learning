from collections import defaultdict

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = defaultdict(int)
        for n in arr:
            d[n] += 1
        
        res = set()
        for k, v in d.items():
            if v in res:
                return False
            res.add(v)
        return True
