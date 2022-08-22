class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        
        num = x
        reverse = 0
        while num >0:
            reverse = reverse*10 + num%10
            num //= 10
            
        
        return reverse == x
        