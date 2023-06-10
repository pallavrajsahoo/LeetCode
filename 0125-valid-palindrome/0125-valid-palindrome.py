class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for ch in s:
            if self.isalpha(ch.lower()):
                new_str += ch.lower()
        return new_str == new_str[::-1]

    
    def isalpha(self, s:str):
            if ord('a') <= ord(s) <= ord('z'):
                return True
            elif ord('0') <= ord(s) <= ord('9'):
                return True
            else:
                return False

        