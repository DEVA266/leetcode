# Last updated: 7/30/2025, 12:23:59 PM
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        elif num < 0 :
            num += 2**32
        m = {10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
        ans = ""
        while(num>0):
            temp = num%16
            if(temp>9):
                ans += m[temp]
            else:
                ans += str(temp)
            num //= 16
        return ans[::-1]

        