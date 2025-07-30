# Last updated: 7/30/2025, 11:57:08 AM
class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for i in range(len(s)-1):
            ans += abs((ord(s[i]) - ord(s[i+1])))
        return ans