class Solution:
    def maxSubArray1(self, nums: List[int]) -> int:
        prefix = [0]
        for elem in nums:
            prefix.append(prefix[-1] + elem)
        maxi = [float('-inf'), 0]
        mini = float('inf')
        for i, elem in enumerate(prefix[1:]):
            if elem >= maxi[0]:
                maxi = elem, i
        for elem in prefix[1:maxi[1]]:
            mini = min(mini, elem)
        return maxi[0] - mini

    def maxSubArray(self, nums):
        # Kardane's algorithm
        max_sum = nums[0]
        curr_sum = nums[0]
        for elem in nums[1:]:
            curr_sum = max(elem, curr_sum + elem)
            max_sum = max(max_sum, curr_sum)
        return max_sum
