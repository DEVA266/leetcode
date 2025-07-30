# Last updated: 7/30/2025, 12:24:32 PM
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while(n>=5):
            n //= 5
            count += n
        return count 
                         

        