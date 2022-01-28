class Solution:
    def lengthOfLongestSubstring(self, s: str)->int:
        if len(s)==0:
            return 0
        word=list()
        unique_character=list()
        res=''
        i=0
        while len(s)>0 and i<len(s):
            if s[i] not in unique_character and s[i] not in word:
                    unique_character.append(s[i])
                    
            else:
                res="".join(unique_character)
                if res=='':
                    break
                s=s[i:]
                unique_character=[]
                i=-1
                if len(res)!=0 and res not in word:
                    word.append(res)
            i+=1
            
        else:
            res="".join(unique_character)
            if len(res)!=0 and res not in word:
                    word.append(res)
        
        longest= len(max(word,key=len))
        return longest
