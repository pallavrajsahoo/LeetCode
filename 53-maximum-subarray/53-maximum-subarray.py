class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        result = nums[0]
        
        for i in nums:
            sum = max(i, sum+i)
            result = max(result, sum)
        
        return result
        