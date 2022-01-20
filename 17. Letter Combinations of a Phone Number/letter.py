# 17. Letter Combinations of a Phone Number [https://leetcode.com/problems/letter-combinations-of-a-phone-number/]
class Solution:
    def findCombinations(self,combinations, digits, previous, index, lettersAndNumbersMapping):
        # Base condition to stop recursion
        if index == len(digits):
            combinations.append(previous)
            return
        # Get the letters corresponding to the current index of digits string
        letters = lettersAndNumbersMapping[int(digits[index])]
        # Loop through all the characters in the current combination of letters
        for i in range(0, len(letters)):
            self.findCombinations(combinations, digits, previous +
                             letters[i], index + 1, lettersAndNumbersMapping)

    def letterCombinations(self, digits: str) :
        # Resultant List
        combinations = list()
        # Base Conditions
        if digits is None or len(digits) == 0:
            return combinations
        # mapping of letters and numbers
        lettersAndNumbersMapping = [
            "0",
            "1",
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz"
        ]
        self.findCombinations(combinations, digits, "", 0, lettersAndNumbersMapping)

        return combinations

sol=Solution()
print(sol.letterCombinations(""))