class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        maxc = 0
        c = 0
        for x in range(len(nums)):
            if nums[x] == 1:
                c += 1
            else:
                c = 0
            maxc = max(maxc , c)
        return maxc
