class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        max_sum = sum([i for i in range(len(nums)+1)])
        return max_sum - sum(nums)