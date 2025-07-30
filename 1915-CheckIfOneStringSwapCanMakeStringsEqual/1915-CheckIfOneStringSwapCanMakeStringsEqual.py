# Last updated: 7/30/2025, 12:22:59 PM
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        i = 0
        j = 0
        swap = 0
        for k in range(len(s1)):
            if s1[k] != s2[k]:
                swap += 1
                if i==0 : i = k
                elif j == 0 : j = k
        if swap == 0:
            return True
        elif swap == 2 and s1[i] == s2[j] and s2[i] == s1[j] :
            return True
        return False