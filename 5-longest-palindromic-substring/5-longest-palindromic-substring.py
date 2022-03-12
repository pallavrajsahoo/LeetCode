class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
#         n = len(s)
#         start = 0
#         max_length = 0
        
#         for current in range(len(s)):
#             right = current + 1
#             left = current - 1
            
#             while right < n and s[right] == s[current]:
#                 right += 1
#             while left >= 0 and s[left] == s[current]:
#                 left -= 1
#             while right < n and left >= 0 and s[left] == s[right]:
#                 left -= 1
#                 right += 1
            
#             current_length = right - left - 1
            
#             if(max_length < current_length):
#                 max_length = current_length
#                 start = left + 1
        
#         return s[start : start+max_length]
        
        start = 0
        length = 1
        for current in range(1, len(s)):
            left = current - length
            right = current + 1
            
            s1 = s[left-1 : right]
            s2 = s[left : right]
            
            if s1 == s1[::-1] and left - 1 >= 0:
                start = left - 1
                length += 2
            elif s2 == s2[::-1]:
                start = left
                length += 1
            
        return s[start : start+length]