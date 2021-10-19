class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myset=set()
        count=0
        ln=len(s)
        left=0
        right=0
        m=0
        for i in range(ln):
            if s[i] in myset:
                while s[left]!=s[i]:
                    myset.remove(s[left])
                    left+=1
                    count-=1
                left+=1  
            else:
                myset.add(s[i])
                right+=1
                count+=1
            if m<count:
                m=count
            
        return m  