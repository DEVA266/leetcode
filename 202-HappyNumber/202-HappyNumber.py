# Last updated: 7/30/2025, 12:24:24 PM
class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        def checking(n):
            if n == 1 :
                return True
            if n in s :
                return False
            s.add(n)
            value = 0
            for i in str(n):
                value += int(i)**2
            return checking(value)

        return checking(n)
        