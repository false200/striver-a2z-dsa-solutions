class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        n = nums[0]
        for x in range(1, len(nums)):
            n ^= nums[x]
        return n