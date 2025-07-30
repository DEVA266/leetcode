# Last updated: 7/30/2025, 12:22:24 PM
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = sum([ i for i in range(1,n+1) if i%m!=0 ])
        num2 = sum([i for i in range(1,n+1) if i%m==0])
        return num1-num2