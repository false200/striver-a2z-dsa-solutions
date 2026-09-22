class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def cnts(n):
            if (n <= 2): return n
            if n in memo: return memo[n]
            memo[n] = cnts(n - 1) + cnts(n - 2)
            return memo[n]
        return cnts(n)
