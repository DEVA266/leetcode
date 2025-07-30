# Last updated: 7/30/2025, 12:24:22 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return False if(len(set(nums)) == len(nums)) else True
        