# Last updated: 7/30/2025, 12:22:28 PM
class Solution:
    def finalString(self, s: str) -> str:
        newstr = ""
        for i in range(len(s)):
            if s[i] == "i":
                newstr = newstr[::-1]
            else:
                newstr += s[i]
        return newstr
