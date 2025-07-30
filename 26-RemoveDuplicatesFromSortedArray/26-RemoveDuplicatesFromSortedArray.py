# Last updated: 7/30/2025, 12:25:03 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        if len(nums) <= 1:
            return len(nums)
        for j in range(1,len(nums)):
            if nums[j] != nums[i-1] :
                nums[i] = nums[j]
                i += 1
        return i