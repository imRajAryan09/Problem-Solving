from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals)
        i=0
        while i<len(intervals)-1:
            print(intervals[i][1],intervals[i+1][0])
            if intervals[i][1]>=intervals[i+1][0]:
                intervals[i][1]=max(intervals[i][1],intervals[i+1][1])
                intervals.pop(i+1)
                i-=1
            i+=1
        return intervals

sol=Solution()
print(sol.merge([[1, 4], [0, 2], [3, 5]]))
