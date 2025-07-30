# Last updated: 7/30/2025, 12:24:55 PM
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = 0
        a,b=int(num1),int(num2)
        while (b>0):
            if b & 1 :
                ans += a
            a = a<<1
            b = b>>1
        return str(ans)
        