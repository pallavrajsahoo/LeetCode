class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        three_sum = 0
        nums.sort()
        min_diff = float('inf')
        result = 0

        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1

            while left<right:
                three_sum = nums[i] + nums[left] + nums[right]
                if three_sum <= target:
                    left += 1
                else:
                    right -= 1
                diff = abs(target - three_sum)
                if min_diff > diff:
                    min_diff = diff
                    result = three_sum
        return result
        






        