# Last updated: 7/30/2025, 12:24:36 PM
from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        m = Counter(nums)
        value = sorted(m.items(), key = lambda i : i[1], reverse = True)
        return value[-1][0]
        
    
        