# Last updated: 7/30/2025, 12:24:18 PM
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        for idx in set(s):
            if t.count(idx) != s.count(idx):
                return False
        return True  
        # if len(s) != len(t):
        #     return False
        # ords = 0
        # ordt = 0
        # for i in range(len(s)):
        #     ords += ord(s[i])
        #     ordt += ord(t[i])
        # if ords != ordt:
        #     return False
        # return True