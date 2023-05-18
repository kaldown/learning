class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def get_power(num):
            i = 0
            while num != 1:
                if not num % 2:
                    num /= 2
                else:
                    num = 3 * num + 1
                i += 1
            return i
        
        transformed = [(get_power(num), num) for num in range(lo, hi+1)]
        return sorted(transformed)[k-1][1]

