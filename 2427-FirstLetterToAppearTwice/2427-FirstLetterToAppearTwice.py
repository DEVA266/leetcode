# Last updated: 7/30/2025, 12:22:40 PM
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        l = []
        for i in s:
            if i in l:
                return i
            else:
                l.append(i)