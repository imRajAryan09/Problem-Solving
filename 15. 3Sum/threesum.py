# 15. 3Sum [https://leetcode.com/problems/3sum/]
class Solution:
    def threeSum(self, nums):
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
            left, right = i+1, n-1
            # loop for remaining pairs
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        return triplets


sol = Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
