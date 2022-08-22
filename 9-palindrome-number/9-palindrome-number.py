class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        reverse = 0
        while num >0:
            digit = int(num%10)
            reverse = reverse*10 + digit
            num //= 10
            
        
        return reverse == x
        