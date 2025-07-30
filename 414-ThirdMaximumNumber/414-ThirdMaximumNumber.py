# Last updated: 7/30/2025, 12:24:00 PM
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n = set(nums)
        if(len(n)<3):
            return max(n)
        n.remove(max(n))
        n.remove(max(n))
        return max(n)
        

        