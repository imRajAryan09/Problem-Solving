class Solution:
    
    def reverse(self, x: int) -> int:
        
        if x>=0:
            ans=int(str(x)[::-1])
            
        else:
            x=x *-1
            ans=int(str(x)[::-1])*-1
            
        if ans>2147483647 or ans<-2147483648:
            ans=0
            
            
        return ans


