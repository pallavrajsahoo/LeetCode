class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap = dict()
        for i, val in enumerate(nums):
            if val in hashmap:
                return val
            else:
                hashmap[val] = i