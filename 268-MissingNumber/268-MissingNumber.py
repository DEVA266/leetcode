# Last updated: 7/30/2025, 12:24:12 PM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = set(range(len(nums)+1))
        return (s-set(nums)).pop()
