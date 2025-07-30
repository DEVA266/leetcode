# Last updated: 7/30/2025, 12:23:04 PM
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # sum = 0
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        return nums