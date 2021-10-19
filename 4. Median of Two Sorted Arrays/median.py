class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        i=j=k=0
        median=0
        len_nums1=len(nums1)
        len_nums2=len(nums2)
        nums_merged=[None]*(len_nums1+len_nums2)
        while i<len_nums1 and j<len_nums2:
            if nums1[i]<nums2[j]:
                nums_merged[k]=nums1[i]
                i+=1
                k+=1
                
            else:
                nums_merged[k]=nums2[j]
                j+=1
                k+=1
                
        while i<len_nums1:
            nums_merged[k]=nums1[i]
            k+=1
            i+=1
            
        while j<len_nums2:
            nums_merged[k]=nums2[j]
            k+=1
            j+=1
            
        len_nums_merged=len_nums1+len_nums2
        
        if len_nums_merged%2==0:
            median=(nums_merged[int(len_nums_merged/2+1)-1]+nums_merged[int(len_nums_merged/2)-1])*0.5       

        else:
            median=nums_merged[int((len_nums_merged+1)/2)-1]

        return median
    
sol=Solution()
print(sol.findMedianSortedArrays([1,3], [2]))