# Last updated: 7/30/2025, 12:22:33 PM
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        s = [True] * (right+1)
        s[0] = False
        s[1] = False

        for i in range(2,int(right**0.5)+1):
            if s[i] :
                for j in range(i*i,right+1,i):
                    s[j] = False
        
        nums = []
        for i in range(left,right+1):
            if s[i] :
                nums.append(i)

        if len(nums) < 2:
            return [-1,-1]

        result = [-1,-1]
        m = float('inf')
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] < m:
                m = nums[i] - nums[i-1]
                result = [nums[i-1],nums[i]]
        return result


        

        