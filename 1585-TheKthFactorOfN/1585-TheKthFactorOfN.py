# Last updated: 7/30/2025, 12:23:11 PM
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
    
        count = 0
        for i in range(1,n+1):
            if n%i==0:
                count += 1
                if count == k:
                    return i
        return -1
        