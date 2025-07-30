# Last updated: 7/30/2025, 12:24:37 PM
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        org = ''.join([i for i in s.lower() if i.isalnum()])
        return org==org[::-1]
        