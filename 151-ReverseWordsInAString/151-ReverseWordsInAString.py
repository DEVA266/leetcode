# Last updated: 7/30/2025, 12:24:33 PM
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.strip().split()[::-1])

        