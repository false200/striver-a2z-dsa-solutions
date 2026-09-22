class Solution:
    def climbStairs(self, n: int) -> int:
        arr = {}
        def cnts(n):
            if (n <= 2): return n
            if n in arr: return arr[n]
            arr[n] = cnts(n - 1) + cnts(n - 2)
            return arr[n]
        return cnts(n)
