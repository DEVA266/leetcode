# Last updated: 7/30/2025, 12:23:43 PM
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.isupper() or word.islower() or word[0].isupper() and word[1:].islower()