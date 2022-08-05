class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()
        for index, value in enumerate(nums):
            temp = target - value
            if temp in map:
                return [map[temp], index]
            else:
                map[value] = index
        