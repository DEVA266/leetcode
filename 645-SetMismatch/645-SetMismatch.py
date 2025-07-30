# Last updated: 7/30/2025, 12:23:40 PM
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        m = {}
        for k in nums:
            m[k] = 1 + m.get(k,0)
        missed = 0
        duplicate = 0
        for i in range(1,len(nums)+1):
            if i not in m :
                missed = i
                continue
            if m[i] > 1 :
                duplicate = i
        return [duplicate,missed]