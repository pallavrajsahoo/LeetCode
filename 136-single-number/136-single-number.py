class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #return 2 * sum(set(nums)) - sum(nums)
        result = 0
        for i in nums:
            result ^= i
        
        return result
        