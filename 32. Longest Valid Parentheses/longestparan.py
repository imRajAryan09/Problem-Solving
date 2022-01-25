class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # to store the longest valid paranthesis
        count = 0
        # left counter to store number of '(' and right counter to store the number of ')'
        left = 0
        right = 0
        # loop through string to take care of extra right paranthesis
        for i in range(len(s)):
            # current character
            c = s[i]
            if c == '(':
                left += 1
            if c == ')':
                right += 1
            # if left==right valid substring
            if left == right:
                count = max(count, left+right)
            # if right>left both counters should be reset
            if right > left:
                left = right = 0
        # reset the counters anyways
        left = right = 0
        # loop through string to take care of extra left paranthesis
        for i in range(len(s)-1, -1, -1):
            # current character
            c = s[i]
            if c == '(':
                left += 1
            if c == ')':
                right += 1
            # if left==right valid substring
            if left == right:
                count = max(count, left+right)
            # if right<left both counters should be reset
            if right < left:
                left = right = 0
        return count
