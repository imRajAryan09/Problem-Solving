# 454. 4Sum II [https://leetcode.com/problems/4sum-ii/]
from typing import List
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        result = 0
        map1, map2, map3, map4 = {}, {}, {}, {}
        for i in nums1:
            map1[i] = map1.get(i, 0) + 1
        for i in nums2:
            map2[i] = map2.get(i, 0) + 1
        for i in nums3:
            map3[i] = map3.get(i, 0) + 1
        for i in nums4:
            map4[i] = map4.get(i, 0) + 1
        log = {}
        for i in map1:
            for j in map2:
                if (-(i+j)) in log:
                    log[0-(i+j)] += map1[i]*map2[j]
                else:
                    log[0-(i+j)] = map1[i]*map2[j]
        for k in map3:
            for l in map4:
                if (k+l) in log:
                    result += log[k+l] * (map3[k]*map4[l])
        return result
