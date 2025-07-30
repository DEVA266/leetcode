# Last updated: 7/30/2025, 1:02:16 PM
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        return [ i+extraCandies>=m for i in candies]
        