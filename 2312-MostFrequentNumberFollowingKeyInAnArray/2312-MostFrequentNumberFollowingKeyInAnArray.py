# Last updated: 7/30/2025, 12:22:48 PM
from collections import Counter
class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        m = {}
        for i in range(len(nums)-1):
            if nums[i] == key :
                if nums[i+1] in m :
                    m[nums[i+1]] += 1
                else :
                    m[nums[i+1]] = 1
                # m[nums[i+1]] = 1 + m.get(nums[i+1],0)
        max_ = 0
        res = 0
        for i,j in m.items():
            if max_ < j:
                max_ = j
                res = i
        return res

            

        