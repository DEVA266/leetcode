# Last updated: 7/30/2025, 12:22:57 PM
class Solution:
    def largestOddNumber(self, num: str) -> str:
        ans = ""
        for i in range(len(num)-1,-1,-1):
            if num[i] in "13579":
                return num[0:i+1]
            else :
                continue     
        return ""      
        