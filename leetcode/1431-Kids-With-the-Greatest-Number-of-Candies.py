class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        highest = max(candies)
        for i, num in enumerate(candies):
            if num + extraCandies >= highest:
                candies[i] = True
            else:
                candies[i] = False
        return candies
