# Last updated: 7/30/2025, 12:23:13 PM
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(0,n):
            ans.extend([nums[i],nums[n+i]])
        return ans