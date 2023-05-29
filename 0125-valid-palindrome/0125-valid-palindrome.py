class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        newS = "".join(ch.lower() for ch in s if ch.isalnum())
       
        return newS == newS[::-1]