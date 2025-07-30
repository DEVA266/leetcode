# Last updated: 7/30/2025, 12:24:26 PM
class Solution:
    def hammingWeight(self, n: int) -> int:
        return (bin(n)[2:]).count('1')