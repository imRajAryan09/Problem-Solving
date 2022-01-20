# 6. Zigzag Conversion [https://leetcode.com/problems/zigzag-conversion/]
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= 1 or numRows == 1:
            return s
        res = [''] * numRows
        periodic = 2 * numRows - 2
        for i in range(len(s)):
            index = i % periodic
            if index <= numRows - 1:
                res[index] += s[i]
            else:
                index = periodic - index
                res[index] += s[i]
        return ''.join(res)
