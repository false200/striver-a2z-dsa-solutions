class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        n = start ^ goal
        c = 0
        while n:
            c += 1
            n = n & (n - 1)
        return c