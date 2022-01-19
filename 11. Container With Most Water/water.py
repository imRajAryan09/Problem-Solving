# 11. Container With Most Water [https://leetcode.com/problems/container-with-most-water/]

from sys import maxsize
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # This variable will store the maximum area
        max_area = -maxsize
        left = 0
        right = len(height)-1
        while left < right:
            height_short = min(height[left], height[right])
            max_area = max(max_area, height_short*(right-left))
            # If their is a longer vertical line present
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
