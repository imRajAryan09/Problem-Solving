from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        while nums[0] != nums[nums[0]]:
            nums[nums[0]], nums[0] = nums[0], nums[nums[0]]
        return nums[0]

sol=Solution()
print(sol.findDuplicate([1,3,4,2,2]))


# class Solution:
    # def findDuplicate(self, nums: List[int]) -> int:
    #     hash = {}
    #     for i in nums:
    #         if i in hash:
    #             return i
    #         else:
    #             hash[i] = 1


# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         nums.sort()
#         for i in range(len(nums) - 1):
#             if nums[i] == nums[i + 1]:
#                 return nums[i]
