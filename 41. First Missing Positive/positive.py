# 41. First Missing Positive [https://leetcode.com/problems/first-missing-positive/]
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # base condition
        if n == 0:
            return 1
        # the number we are looking for belongs to the
        # set {1...len(nums)+1}
        # an array(indicator[]) to store the occurence
        # of every element in nums indicator contains n+1 0's,
        # one for each number in the set {1...len(nums)+1}
        indicator = [0]*(n+1)
        # for all positive number occurences in nums[]
        # we map 1 at the index of that number in indicator[]
        for i in range(0, n):
            if nums[i] > 0 and nums[i] <= n:
                indicator[nums[i]] = 1
        # the first index that is equal to 0 is the first missing +ve
        for i in range(1, n+1):
            if indicator[i] == 0:
                return i
        return n+1


sol = Solution()
print(sol.firstMissingPositive(nums=[1, 2, 0]))
