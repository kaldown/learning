class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [n]
        
        result = []
        for x in range(n+1):
            result.append(bin(x)[2:].count('1'))
        
        return result
