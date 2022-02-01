# 50. Pow(x, n)[https://leetcode.com/problems/powx-n/]
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n == -1:
            return 1 / x
        if n == 1:
            return x
        temp = self.myPow(x, int(n/2))
        if(n % 2 == 0):
            return temp*temp
        else:
            if n > 0:
                return x*temp*temp
            else:
                return (temp*temp)/x
