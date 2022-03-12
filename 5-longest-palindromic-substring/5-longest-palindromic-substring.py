class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start = 0
        max_length = 0
        
        for current in range(len(s)):
            right = current + 1
            left = current - 1
            
            while right < n and s[right] == s[current]:
                right += 1
            while left >= 0 and s[left] == s[current]:
                left -= 1
            while right < n and left >= 0 and s[left] == s[right]:
                left -= 1
                right += 1
            
            current_length = right - left - 1
            
            if(max_length < current_length):
                max_length = current_length
                start = left + 1
        
        return s[start : start+max_length]