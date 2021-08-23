class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x==0:
            return True
        
        if x<0:
            return False
        
        reverse=0
        y=x
        
        while y>0:
            r=y%10
            reverse=reverse*10+r
            y//=10
        
        if reverse>2147483647 or reverse<-2147483648:
            return False
        
        if x==reverse:
            return True
        
        else:
            return False