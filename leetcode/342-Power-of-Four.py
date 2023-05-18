class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 0:
            return False
        
        n = float(n)
        while str(n).split('.')[1] == '0':
            n /= 4
            if n == 1:
                return True
        return False
