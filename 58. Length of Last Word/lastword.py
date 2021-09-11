class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count=0
        l_words=list()
        word=''
        if s[len(s)-1]!=' ':
            s+=' '
        for i in range(len(s)):
            if s[i]!=' ':
                word+=s[i]
            else:
                l_words.append(word)
                word=''
                
        # Remove multiple empty spaces from string List
        # Using list comprehension + strip()
        l_no_spaces = [ele for ele in l_words if ele.strip()]
                
        return l_no_spaces[-1]
            
        
sol=Solution()
print(sol.lengthOfLastWord("luffy is still joyboy"))