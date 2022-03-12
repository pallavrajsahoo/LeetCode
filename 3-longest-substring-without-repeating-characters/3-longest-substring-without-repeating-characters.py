class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        maxlen = 0
        l = 0
        for r, val in enumerate (s):
            if val in used and l <= used[val]:
                l = used[val] + 1
            else:
                maxlen = max(maxlen, r-l+1)
            used[val] = r
        
        return maxlen
            
        