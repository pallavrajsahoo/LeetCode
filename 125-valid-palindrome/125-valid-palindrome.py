class Solution:
    def isPalindrome(self, s: str) -> bool: 
        new = re.sub(r'[^a-zA-Z0-9]', "", s.lower())
        
        return new == new[::-1]
        
        