# Last updated: 7/30/2025, 12:22:32 PM
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        p,n = 0,0
        for i in nums :
            if i > 0 :
                p += 1
            elif i < 0 :
                n += 1
        return max(p,n)