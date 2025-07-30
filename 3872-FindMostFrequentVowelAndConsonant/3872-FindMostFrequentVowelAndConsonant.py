# Last updated: 7/30/2025, 11:56:55 AM
class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        vowel = "aeiou"
        vowels = [0]*26
        const = [0]*26 
        for ch in s:
            id = ord(ch) - ord('a')
            if ch in vowel :
                vowels[id] += 1
            else :
                const[id] += 1
        return max(vowels)+max(const)