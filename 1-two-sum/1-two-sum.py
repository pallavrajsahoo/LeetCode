class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()
        for index, val in enumerate(nums):
            temp = target - val
            if temp in map:
                return [map[temp], index]
            else:
                map[val] = index