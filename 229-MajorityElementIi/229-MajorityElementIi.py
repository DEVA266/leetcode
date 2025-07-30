# Last updated: 7/30/2025, 12:24:19 PM
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        m = Counter(nums)
        for w,f in m.items():
            if f > len(nums)//3:
                ans.append(w)
        return ans