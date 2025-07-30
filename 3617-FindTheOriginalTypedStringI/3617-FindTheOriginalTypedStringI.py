# Last updated: 7/30/2025, 11:57:01 AM
class Solution:
    def possibleStringCount(self, word: str) -> int:
        if len(word) == 1:
            return 1
        elif len(word) >= 1 :
            output = 1
        for i in range(len(word)-1):
            if word[i] == word[i+1]:
                output += 1
        return output