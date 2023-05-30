class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lookup = dict()
        for i, val in enumerate(numbers):
            temp = target - val
            if temp in lookup:
                return [lookup[temp], i+1]
            else:
                lookup[val] = i+1