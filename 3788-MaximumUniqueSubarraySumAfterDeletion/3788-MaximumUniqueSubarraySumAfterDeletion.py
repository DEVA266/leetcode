# Last updated: 7/30/2025, 11:57:07 AM
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if(max(nums)<0):
            return max(nums)
        n = []
        sums = 0
        for i in nums:
            if i not in n and i>0:
                n.append(i)
                sums += i
        return sums
        