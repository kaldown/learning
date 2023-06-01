class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        def can_place(i):
            if flowerbed[i-1:i] in [[], [0]] and flowerbed[i+1:i+2] in [[], [0]]:
                return True
            return False

        for i in range(len(flowerbed)):
            is_set = flowerbed[i]
            if is_set:
                continue
            if can_place(i):
                flowerbed[i] = 1
                n -= 1
            if not n:
                return True
        return n <= 0

