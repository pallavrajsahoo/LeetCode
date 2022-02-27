class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
       
        if s == "":
            return True
        pos = 0
        for char in t:
            if pos <= len(s) - 1:
                if char == s[pos]:
                    pos += 1
                    
        if pos == len(s):
            return True
        return False
    
        