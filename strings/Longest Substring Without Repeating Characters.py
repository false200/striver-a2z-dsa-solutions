class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l , r = 0 , 0
        m = len(s)
        saw = set()
        maxv = 0
        while (r < m):
            if s[r] not in saw:
                maxv = max(maxv , r - l + 1)
                saw.add(s[r])
                r += 1
            else:
                while s[r] in saw:
                    saw.remove(s[l])
                    l += 1
        return maxv