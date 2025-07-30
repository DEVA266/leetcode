# Last updated: 7/30/2025, 12:23:27 PM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([ i*i for i in nums])