class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = max(nums)
        flag = 0

        for num in nums:
            if largest == num:
                continue
            else:
                if num*2 > largest:
                    flag = 1
        
        if flag == 1:
            return -1
        else:
            return nums.index(largest)
