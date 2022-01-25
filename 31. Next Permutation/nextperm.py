# 31. Next Permutation [https://leetcode.com/problems/next-permutation/]

from typing import List


class Solution:
    def reverse(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # length of the array
        n = len(nums)
        # index of the first element that
        # is smaller that the element to its right
        index = -1
        for i in range(n-1, 0, -1):
            if nums[i] > nums[i-1]:
                index = i-1
                break
        # base condition
        if index == -1:
            self.reverse(nums, 0, n-1)
            return
        j = n-1
        # Again swap from right to left to find first element
        # that is greater than the above find
        for i in range(n - 1, index, -1):
            if nums[i] > nums[index]:
                j = i
                break
        # Swap the elements
        nums[index], nums[j] = nums[j], nums[index]
        # Reverse the elements from index + 1 to the nums.length
        self.reverse(nums, index + 1, n - 1)
