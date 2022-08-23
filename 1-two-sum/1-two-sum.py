class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = dict()
        
        for index, val in enumerate(nums):
            temp = target - val
            if temp in result:
                return [result[temp], index]
            else:
                result[val] = index
            
        