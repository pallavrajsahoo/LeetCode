class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = []
        length = 0
        left = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
                
            char_set.append(s[right])
            length = max(length, len(char_set))

        return length



            
        