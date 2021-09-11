class Solution:
    def searchInsert(self, nums, target: int) -> int:
        low = 0
        high = len(nums) - 1
        mid = 0
        count=1
        
        while low <= high:
            
            count+=1
            mid=low + (high - low)//2  
            
            # If x is greater, ignore left half
            if nums[mid] < target:
                low = mid + 1
    
            # If x is smaller, ignore right half
            elif nums[mid] > target:
                high = mid - 1
    
            # means x is present at mid
            else:
                return mid
    
        # If we reach here, then the element was not present
        return low
    
sol=Solution()
print(sol.searchInsert([1],0))