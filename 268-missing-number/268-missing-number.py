class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        s = sum([i for i in range(len(nums)+1)])
        t = sum([i for i in nums])
        
        return s-t
        