class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0:
            return True
        if len(t)==0:
            return False
        fin=len(s)
        j=0
        for i in t:
            if i==s[j]:
                j+=1 #If we find one letter from s, we hop on to find next
                if j==fin: #If all the letters from s are covered, that means our work here is done.
                    return True
        return False
        