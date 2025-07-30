# Last updated: 7/30/2025, 12:23:53 PM
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s1 = set(nums)
        s2 = set((range(1,len(nums)+1)))
        return list(s2-s1)