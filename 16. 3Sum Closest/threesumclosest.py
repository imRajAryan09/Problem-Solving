# 15. 16. 3Sum Closest [https://leetcode.com/problems/3sum-closest/]
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Sort the given array
        nums.sort()
        # length of the array
        n = len(nums)
        # closest value
        closest = nums[0]+nums[1]+nums[n-1]
        # loop for each elements in the array
        for i in range(0, n-2):
            # left and right pointers
            left, right = i+1, n-1
            # loop for remaining pairs
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum <= target:
                    left += 1
                else:
                    right -= 1
                if abs(closest - target) > abs(current_sum - target):
                    closest = current_sum
        return closest


sol = Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
