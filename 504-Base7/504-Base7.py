# Last updated: 7/30/2025, 12:23:50 PM
class Solution:
    def convertToBase7(self, num: int) -> str:
        ans = ""
        temp = abs(num)
        while(temp>0):
            ans = str(temp%7) + ans
            temp //= 7
        if num==0 :
            return "0"
        elif num>0:
            return ans
        else:
            return "-" + ans

        