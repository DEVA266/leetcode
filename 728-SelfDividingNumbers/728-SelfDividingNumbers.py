# Last updated: 7/30/2025, 12:23:36 PM
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        nums = []
        for i in range(left,right+1):
            temp = i
            ans = True
            while(temp>0):
                last = temp%10
                if(last == 0 or i%last != 0 ):
                    ans = False
                    break
                temp //= 10
            if ans :
                nums.append(i)
        return nums