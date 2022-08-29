class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = sum([i for i in range(n+1)])
        return max_sum - sum(nums)