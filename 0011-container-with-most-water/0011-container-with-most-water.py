class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height)-1

        while left < right:
            max_area = max((right-left)*min(height[right],height[left]), max_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

        