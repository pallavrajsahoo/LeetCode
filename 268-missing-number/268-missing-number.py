class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        x = sum([i for i in range(len(nums)+1)])
        y = sum([i for i in nums])
        
        return x-y
        