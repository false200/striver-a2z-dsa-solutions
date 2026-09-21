class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        def lps(patt):
            m = len(patt)
            lps = [0] * m
            length = 0 
            i = 1

            while i < m:
                if patt[i] == patt[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        def kmps(text, patt):
            n = len(text)
            m = len(patt)
            
            if m == 0: return False

            lpsr = lps(patt)

            i = 0  
            j = 0  
            while i < n:
                if text[i] == patt[j]:
                    i += 1
                    j += 1

                if j == m:
                    return True     
                elif i < n and text[i] != patt[j]:
                    if j != 0:
                        j = lpsr[j - 1]    
                    else:
                        i += 1            
            return False
        
        return kmps(s + s, goal)