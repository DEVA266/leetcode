# Last updated: 7/30/2025, 12:23:02 PM
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        s = [sum(i) for i in accounts]
        return max(s)