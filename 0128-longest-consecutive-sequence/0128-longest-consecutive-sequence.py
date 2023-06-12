class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_count = 0
        count = 1

        for num in num_set:
            if num-1 not in num_set:
                count = 1
                temp = num+1
                while temp in num_set:
                    count += 1
                    temp += 1
            
            max_count = max(max_count, count)
        
        return max_count

        