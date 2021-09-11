class Solution:      
    def isValid( self,s: str) -> bool:
        
        balanced = True
        index = 0
        l1=[]
        
        while index < len(s) and balanced:
            
            symbol = s[index]
            
            if symbol in "({[":
                l1.append(symbol)
                
            else:
                if len(l1)==0:
                    balanced = False
                    
                else:
                    top = l1.pop()
                    opens = "([{"
                    closes = ")]}"
                    ans=opens.index(top) == closes.index(symbol)
                    
                    if ans==False:
                        balanced = False

            index = index + 1

        if balanced and len(l1)==0:
            return True
        
        else:
            return False