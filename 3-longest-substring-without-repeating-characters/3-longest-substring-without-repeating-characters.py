class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = dict()
        max_length, l = 0, 0
        for r, letter in enumerate(s):
            if letter in used and l <= used[letter]:
                l = used[letter] + 1
            else:
                max_length = max(max_length, r - l + 1)

            used[letter] = r


        return max_length
