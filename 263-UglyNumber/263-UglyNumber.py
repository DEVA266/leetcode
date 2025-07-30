# Last updated: 7/30/2025, 12:24:13 PM
class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0 :
            return False
        for i in [2,3,5]:
            while n%i==0:
                n //= i
        return n == 1
        
