class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums = sorted(nums)
        for i, num in enumerate(nums[:-1]):
            if num == nums[i+1]:
                return True
        return False

