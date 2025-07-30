# Last updated: 7/30/2025, 12:24:47 PM
class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x
        while start<=end:
            mid = start + (end-start) // 2
            if x == (mid*mid):
                return mid
            elif x > (mid*mid) :
                start = mid + 1
            else :
                end = mid-1
        return end
        
            