class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        for i in set(s):
            if i not in t:
                return False
            else:
                if s.count(i) != t.count(i):
                    return False
        return True
        