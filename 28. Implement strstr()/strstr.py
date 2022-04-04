class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="" or haystack==needle:
            return 0
        if len(haystack)!=0:
            for i in range(len(haystack)):
                if needle[0]==haystack[i] and i+len(needle)<=len(haystack):
                    part=haystack[i:i+len(needle)]
                    if part==needle:
                        return i
        return -1
               
