class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        ans = [0] * 26

        for x in range(len(s)):
            ans[ord(s[x]) - ord('a')] += 1
            ans[ord(t[x]) - ord('a')] -= 1

        for x in ans:
            if x != 0:
                return False

        return True