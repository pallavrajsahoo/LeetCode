class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        total = sum([i for i in range(1, len(nums)+1)])
        
        return total - sum(nums)