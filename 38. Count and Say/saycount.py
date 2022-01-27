class Solution:
    def countAndSay(self, n: int) -> str:
        # Base Case
        res = '1'
        # looping from 1 till the (n-1)th integer
        for i in range(1, n):
            # when n increments all the variables(prev,count,curr_str) will be reinitialized
            prev, count = '.', 0
            curr_str = ""
            # looping through the string
            for char in res:
                # if char == prev or prev == '.'
                # (in case of the first occurence of new characters)
                # count will increment by 1
                if char == prev or prev == '.':
                    count += 1
                # if char != prev then curr_str will be appended with the count and prev
                else:
                    curr_str += str(count) + prev
                    # reinitializing the variables
                    count = 1
                # updating the prev
                prev = char
            # appending the last count and prev to curr_str
            curr_str += str(count) + prev
            # updating the res
            res = curr_str
        return res

# Here time complexity can’t be fixed because if we take N > 30
# then its never possible to store the output string so
# for worst-case scenario time complexity is O(10 ^ 6).

