from heapq import heappush, heappop

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        h = []
        for d, s in list(zip(dist, speed)):
            heappush(h, (d/s))

        # kill first one insta
        heappop(h)

        i = 1
        count = 1
        while h:
            d = heappop(h)
            if d <= i:
                return count
            i += 1
            count += 1
        return len(dist)
