# Last updated: 7/30/2025, 12:25:02 PM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums :
            nums.remove(val)
        return len(nums)