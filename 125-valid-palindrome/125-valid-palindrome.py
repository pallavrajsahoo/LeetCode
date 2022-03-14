class Solution:
    def isPalindrome(self, s: str) -> bool:
         
        new = "".join(s.split(" ")).lower()
        pal = ""
        for char in s:
            if char.isalnum():
                pal += char

        return pal.lower() == pal[::-1].lower()
        
        