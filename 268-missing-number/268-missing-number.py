class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        a = sum([i for i in range(len(nums)+1)])
        b = sum([i for i in nums])
        
        return a-b
        