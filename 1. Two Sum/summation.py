class Solution:
    
    def twoSum(self, nums, target: int) -> int:
        // two loops to check the sum
        for i in range(len(nums)):
            
            for j in range(i+1,len(nums)):
                
                if nums[i]+nums[j]==target:
                    return i,j
        
