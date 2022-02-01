# 49. Group Anagrams [https://leetcode.com/problems/group-anagrams/]
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        result = []
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in groups:
                groups[sorted_word].append(word)
            else:
                groups[sorted_word] = [word]
        for key, value in groups.items():
            result.append(value)
        return result
