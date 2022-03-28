from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def subsetRecurse(subset, start):
            subsets.append(list(subset))
            for idx in range(start, len(nums)):
                if idx != start and nums[idx] == nums[idx-1]:
                    continue
                subset.append(nums[idx])
                subsetRecurse(subset, idx+1)
                # backtrack
                subset.pop()
        nums.sort()
        subsets = []
        subsetRecurse([], 0)
        return subsets
