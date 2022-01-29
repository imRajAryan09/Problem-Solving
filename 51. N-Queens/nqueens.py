# 51. N-Queens [https://leetcode.com/problems/n-queens/]
from typing import List


class Solution:
    """
    example on the left : [1,3,0,2]
    example on the right: [2,0,3,1]
    """

    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        state = []
        self.search(state, solutions, n)
        return solutions

    def is_valid_state(self, state, n):
        # check if it is a valid solution
        return len(state) == n

    def get_candidates(self, state, n):
        if not state:
            return range(n)
        # find the next position in the state to populate
        position = len(state)
        candidates = set(range(n))
        # prune down candidates that place the queen into attack
        for row, col in enumerate(state):
            # discard the column index if it is occupied by the queen
            candidates.discard(col)
            # discard the diagonal index if it is occupied by the queen
            dist = position-row
            # for bigger diagonaal col+dist
            candidates.discard(col+dist)
            # for smaller diagonaal col-dist
            candidates.discard(col-dist)
        return candidates

    def search(self, state, solutions, n):
        if self.is_valid_state(state, n):
            state_string = self.state_to_string(state, n)
            solutions.append(state_string)
            return
        for candidate in self.get_candidates(state, n):
            # recurse
            state.append(candidate)
            self.search(state, solutions, n)
            state.pop()

    def state_to_string(self, state, n):
        # ex. [1, 3, 0, 2]
        # output: [".Q..","...Q","Q...","..Q."]
        ret = []
        for i in state:
            string = '.'*i+'Q'+'.'*(n-i-1)
            ret.append(string)
        return ret
