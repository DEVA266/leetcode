# Last updated: 7/30/2025, 12:23:56 PM
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        m = 0
        for i in nums:
            if i:
                count += 1
                if count > m:
                    m = count
            else :
                count = 0
        return m

                
        