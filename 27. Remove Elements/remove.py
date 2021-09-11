class Solution:
    def removeElement(self, nums, val: int) -> int:
        
        # Counter for keeping track of elements other than val
        count = 0
        
        # Loop through all the elements of the array
        for i in range(len(nums)):
            
            if nums[i] != val:
                # If the element is not val
                nums[count] = nums[i]
                count += 1
                
        return count
    
sol=Solution()
print(sol.removeElement([3,2,2,3],3))
            
        