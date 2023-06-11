class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        char_set = set()
        left = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            length = max(length, len(char_set))
        
        return length