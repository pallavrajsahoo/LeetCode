class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        
        if n == 0:
            return True
        
        i = 0
        for c in t:
            if c == s[i]:
                i += 1
                if i == n:
                    return True
        
        return False
        