# 15. 3Sum [https://leetcode.com/problems/3sum/]
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the given array
        nums.sort()
        # length of the array
        n = len(nums)
        # resultant list
        triplets = list()
        # loop for each elements in the array
        for i in range(0, n):
            # avoid duplicates due to i
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # left and right pointers
            j, k = i+1, n-1
            # loop for remaining pairs
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
        return triplets
