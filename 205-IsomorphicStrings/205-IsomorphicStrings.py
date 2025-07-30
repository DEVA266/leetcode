# Last updated: 7/30/2025, 12:24:20 PM
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        m = {}
        for i in range(len(s)):
            if s[i] in m.keys():
                if m[s[i]] != t[i]:
                    return False
            else : 
                if t[i] in m.values():
                    return False
                m[s[i]] = t[i]
        return True

        