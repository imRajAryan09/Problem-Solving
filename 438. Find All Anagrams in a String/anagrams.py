# 438. Find All Anagrams in a String [https://leetcode.com/problems/find-all-anagrams-in-a-string/]
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # if the length of string is greater than
        # the length of pattern then no anagrams
        # are possible 
        if len(p) > len(s):
            return []
        pCount, sCount = {}, {}
        # mapping from index 0 to len(p)
        for i in range(len(p)):
            pCount[p[i]] = 1+pCount.get(p[i], 0)
            sCount[s[i]] = 1+sCount.get(s[i], 0)
        res = [0] if sCount == pCount else []
        l = 0
        for r in range(len(p), len(s)):
            sCount[s[r]] = 1+sCount.get(s[r], 0)
            sCount[s[l]] -= 1
            if sCount[s[l]]==0:
                sCount.pop(s[l])
            l+=1
            if sCount==pCount:
                res.append(l)
        return res


sol = Solution()
print(sol.findAnagrams(s="cbaebabacd", p="abc"))
