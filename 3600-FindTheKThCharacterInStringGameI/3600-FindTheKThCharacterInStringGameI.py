# Last updated: 7/30/2025, 11:57:10 AM
class Solution:
    def kthCharacter(self, k: int) -> str:
        return chr(ord('a') + bin(k-1)[2:].count('1'))