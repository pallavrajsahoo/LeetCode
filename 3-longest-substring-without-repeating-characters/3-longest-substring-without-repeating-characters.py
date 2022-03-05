class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        maxLen = 0
        i = 0
        j = 0
        while(j < len(s)):
            if s[j] not in hashset:
                hashset.add(s[j])
                j += 1
                maxLen = max(len(hashset), maxLen)
            else:
                hashset.remove(s[i])
                i += 1
                
        return maxLen
            
        