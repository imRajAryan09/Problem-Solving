class Solution:
    def removeDuplicates(self, nums) -> int:
        
        n=len(nums)
        if n == 0 or n == 1:
            return n

        # To store index of next
        # unique element
        j = 0

        # Doing same as done
        # in Method 1 Just
        # maintaining another 
        # updated index i.e. j
        for i in range(0, n-1):
            
            if nums[i] != nums[i+1]:
                nums[j] = nums[i]
                j += 1

        // j is number of unique elements
        nums[j] = nums[n-1]
        j += 1
        return j
        
    

sol=Solution()
print(sol.removeDuplicates([1,1,2]))
