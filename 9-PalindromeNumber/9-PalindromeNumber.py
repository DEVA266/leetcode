# Last updated: 7/30/2025, 12:25:07 PM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        x = str(x)
        if x == x[::-1] :
            return True
        else :
            return False
