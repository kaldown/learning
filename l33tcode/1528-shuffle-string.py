from heapq import heappush, heappop

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        d = {}
        result = []
        for i, char in enumerate(s):
            heappush(result, (indices[i], char))
        return ''.join([heappop(result)[1] for _ in range(len(result))])
