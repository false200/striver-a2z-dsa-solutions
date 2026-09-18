class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        m = len(nums)
        i = 1 << m
        glob = []
        for x in range(i):
            lis = []
            for y in range(m):
                if (x & (1 << y)) != 0:
                    lis.append(nums[y])
            glob.append(lis)
        return glob