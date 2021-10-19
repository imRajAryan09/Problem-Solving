class Solution:
    def plusOne(self, digits):
        num=0
        for i in range(len(digits)):
            num+=(10**i)*digits[len(digits)-i-1]
            
        num+=1
        str_num=str(num)
        digi_incre=list()
        for i in range(len(str_num)):
            digi_incre.append(str_num[i])
            
        return digi_incre
            
        
sol=Solution()
print(sol.plusOne([9]))