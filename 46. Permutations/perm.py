# 46. Permutations [https://leetcode.com/problems/permutations/]
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        len_n = len(nums)

        def backtrack(my_nums, use_nums):
            if len(my_nums) == len_n:
                results.append(my_nums)
                return
            for i in range(len(use_nums)):
                x = my_nums.copy()
                x.append(use_nums[i])
                backtrack(x, use_nums[:i]+use_nums[i+1:])
        self.backtrack([], nums)
        return results
