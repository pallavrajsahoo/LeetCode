class Solution:
    def isPalindrome(self, s: str) -> bool:
         
        new = "".join(s.split(" "))
        pal = ""
        for char in s:
            if char.isalnum():
                pal += char

        return pal.lower() == pal[::-1].lower()
        
        