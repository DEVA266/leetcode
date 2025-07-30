# Last updated: 7/30/2025, 12:24:09 PM
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [(bin(i)[2:]).count('1')  for i in range(0,n+1)]
        return ans
