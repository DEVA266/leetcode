# Last updated: 7/30/2025, 12:24:06 PM
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = Counter(nums)
        # for i in set(nums):
        #     m[i] = nums.count(i)
        sorted_m = (sorted(m.items(), key=lambda i : i[1] , reverse = True))
        ans = []
        for i in range(0,k):
            ans.append(sorted_m[i][0])
        return ans


         