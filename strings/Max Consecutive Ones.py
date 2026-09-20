class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        l = 0
        maxv = 0
        for x in range(len(nums)):
            if nums[x] == 1:
                maxv = max(maxv, x - l + 1)
            else:
                l = x + 1
        return maxv