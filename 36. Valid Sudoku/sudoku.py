# 36. Valid Sudoku [https://leetcode.com/problems/valid-sudoku/]
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # set to store all the occurences of numbers
        seen = set()
        # loop through the 9*9 matrix by using nested loops
        for i in range(9):
            for j in range(9):
                # current element
                c = board[i][j]
                if c == '.':
                    continue
                # if c is a number, store it in a set so if the number reappears  
                # the validation fails and False is returned.
                if c + '@row ' + str(i) in seen or \
                        c + '@col ' + str(j) in seen or \
                        c + '@box ' + str(i // 3) + str(j // 3) in seen:
                    return False
                # if the validations pass, add c to the set for upcoming iterations
                seen.add(c + '@row ' + str(i))
                seen.add(c + '@col ' + str(j))
                seen.add(c + '@box ' + str(i // 3) + str(j // 3))
        return True
