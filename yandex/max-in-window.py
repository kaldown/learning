# given array of nums and k,
# return the max number on each window.
# nums = [1, 0, 3, 6, 2, 5], k = 3
# 1, 0, 3 -> 3
# 0, 3, 6 -> 6
# 3, 6, 2 -> 6
# 6, 2, 5 -> 6
# result: [3, 6, 6, 6]


def solution(nums: list[int], k: int) -> list[int]:
    if not nums:
        return []

    result = []
    for i in range(len(nums) - k + 1):
        result.append(max(nums[i:i+k]))
    return result


assert solution(nums=[1, 0, 3, 6, 2, 5], k=3) == [3, 6, 6, 6]

