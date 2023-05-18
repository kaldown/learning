# Given:
#     sorted numbers array
# Return:
#     sorted pow of 2 such numbers
# Ex:
#     1, 2, 3
#     1, 4, 9

from heapq import heappush, heappop

def solution(nums: list[int]) -> list[int]:
    h = []
    for num in nums:
        heappush(h, pow(num, 2))
    return [heappop(h) for _ in range(len(h))]

assert solution([1, 2, 3]) == [1, 4, 9]
assert solution([-5, 1, 2, 3]) == [1, 4, 9, 25]

