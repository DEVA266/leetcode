# Last updated: 7/30/2025, 12:24:10 PM
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        m = {}
        string = s.split()
        if len(pattern) != len(string):
            return False

        for i in range(len(pattern)) :
            if pattern[i] in m.keys():
                if m[pattern[i]] != string[i]:
                    return False
                else:
                    continue

            if string[i] in m.values():
                return False            
            m[pattern[i]] = string[i]
        return True

