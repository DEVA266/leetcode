# Last updated: 7/30/2025, 12:22:31 PM
class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums)<3:
            return -1
        return sorted(nums[:3])[1]

