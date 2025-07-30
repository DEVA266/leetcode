# Last updated: 7/30/2025, 12:23:05 PM
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def sum(n):
            s = 0
            while(n!=0):
                # last = n%10
                s += n%10
                n //=10
            return s
        m = {}
        for i in range(lowLimit,highLimit+1):
            value = sum(i)
            m[value] = 1 + m.get(value,0)
        return max(m.values())
            

         