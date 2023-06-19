class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        zeros = 0
        for i, num in enumerate(nums):
            if num != 0:
                # swap
                nums[zeros], nums[i] = num, nums[zeros]
                zeros += 1
        return

