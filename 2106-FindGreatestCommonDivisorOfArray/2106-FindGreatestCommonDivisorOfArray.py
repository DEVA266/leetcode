# Last updated: 7/30/2025, 12:22:58 PM
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        high = max(nums)
        low = min(nums)
        while(low!=0):
            high,low = low,high%low
        return high