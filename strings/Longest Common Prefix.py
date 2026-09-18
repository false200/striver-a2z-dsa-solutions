class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        com = strs[0]
        runs = len(com) - 1
        for x in range(1, len(strs)):
            t = strs[x]
            r = 0
            e = min(len(t) - 1, runs)
            while r <= e and t[r] == com[r]:
                r += 1
            runs = min(r - 1, runs)
        return com[:runs + 1]