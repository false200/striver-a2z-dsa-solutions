class Solution:
    def longestKSubstr(self, s, k):
        freq = {}
        l , r = 0 , 0
        m = len(s)
        maxv = -1

        while (r < m):
            freq[s[r]] = freq.get(s[r] , 0 )  + 1
            while len(freq) > k:
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1
            if len(freq) == k:
                maxv = max(maxv, r - l + 1)
            r += 1

        return maxv