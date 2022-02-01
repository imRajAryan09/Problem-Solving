# 48. Rotate Image [https://leetcode.com/problems/rotate-image/]
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix)-1
        while left < right:
            for i in range(right-left):
                top, bottom = left, right
                # save the top-left value
                top_left = matrix[top][left+i]
                # move the bottom-left into top-left
                matrix[top][left+i] = matrix[bottom-i][left]
                # move the bottom-right to bottom-left
                matrix[bottom-i][left] = matrix[bottom][right-i]
                # move the top-right to the bottom-right
                matrix[bottom][right-i] = matrix[top+i][right]
                # move the top-left to top-right
                matrix[top+i][right] = top_left
            right -= 1
            left += 1
