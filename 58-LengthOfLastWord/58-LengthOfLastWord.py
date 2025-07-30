# Last updated: 7/30/2025, 12:24:52 PM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])