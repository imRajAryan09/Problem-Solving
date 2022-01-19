# 8. String to Integer (atoi) [https://leetcode.com/problems/string-to-integer-atoi/]

class Solution:
    def myAtoi(self, s: str) -> int:
        # Base condition
        if len(s) < 1 or s is None:
            return 0
        # Max and Min values for the integers
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        # Trimmed String
        #   Python has lstrip() method which removes all the whitespaces from
        #   left part of the string. In other languages such as JAVA we would
        #   have to use RegEx to do this.
        #            str = str.replaceAll("^\\s+", "");
        s = s.lstrip()
        # counter
        i = 0
        # Flag to indicate if the number is -ve
        isNegative = len(s) > 1 and s[0] == '-'
        # Flag to indicate if the number is +ve
        isPositive = len(s) > 1 and s[0] == '+'
        if isNegative or isPositive:
            i += 1
        # to store the converted number
        number = 0
        # Loop for each numeric character in the string iff numeric characters are leading
        # characters in the string
        while i < len(s) and '0' <= s[i] <= '9':
            number = number * 10 + (ord(s[i]) - ord('0'))
            i += 1
        # Give back the sign to the number
        if isNegative:
            number *= (-1)
        # Edge Cases- integer overflow and underflow
        if number < INT_MIN:
            return INT_MIN
        if number > INT_MAX:
            return INT_MAX
        return number


sol = Solution()
print(sol.myAtoi("42"))
