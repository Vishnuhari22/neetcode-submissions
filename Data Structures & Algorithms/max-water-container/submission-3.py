class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        area_max = 0

        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            area_max = max(area, area_max)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            
        return area_max