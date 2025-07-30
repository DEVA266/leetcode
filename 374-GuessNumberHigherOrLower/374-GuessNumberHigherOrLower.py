# Last updated: 7/30/2025, 12:24:05 PM
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        st=1
        end=n
        mid=0
        while(st<=end):
            mid=st+(end-st)//2
            r = guess(mid)
            if(r==0): return mid
            elif(r==1): st=mid+1
            else: end=mid-1
        return st