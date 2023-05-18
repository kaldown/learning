class Solution:
    def sumOfUnique1(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        return sum([k for k,v in d.items() if v == 1])
