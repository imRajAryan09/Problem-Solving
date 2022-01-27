# 39. Combination Sum [https://leetcode.com/problems/combination-sum/submissions/]
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # creating a 1D array
        cache = [[] for _ in range(target + 1)]
        # Base Case
        cache[0] = [[]]
        # looping through the candidates
        for c in candidates:
            for i in range(target + 1):
                if i >= c:
                    for temp_ans in cache[i - c]:
                        cache[i].append(temp_ans + [c])
        return cache[-1]
