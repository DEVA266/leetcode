# Last updated: 7/30/2025, 12:22:36 PM
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        ans = []
        for i in range(1,min(a,b)+1):
            if a%i==0 and b%i==0:
                ans.append(i)
        return len(ans)

        