class Solution:
    def maxDepth(self, s: str) -> int:
        cn = 0
        maxcn = 0
        for x in range(len(s)):
            d = s[x]
            if d == "(" or d == "[" or d == "{":
                cn += 1
            if d == ")" or d == "]" or d == "}":
                cn -= 1
            maxcn = max(maxcn, cn)
        return maxcn