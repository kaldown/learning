class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d = {}
        for number in arr:
            if number in d:
                d[number] += 1
            else:
                d[number] = 1
        result = sorted(d.items(), key=lambda item: item[1])
        accum = 0
        for i, tupl in enumerate(result):
            _, w = tupl
            accum += w
            if accum == k:
                # removed all the numbers
                return len(set(result[i+1:]))
            elif accum > k:
                # some numbers left repeating
                return len(set(result[i:]))
