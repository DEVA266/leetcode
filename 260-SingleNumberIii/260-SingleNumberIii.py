# Last updated: 7/30/2025, 12:24:14 PM
from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        m = Counter(nums)
        value = sorted(m.items(), key=lambda i : i[1], reverse = True)
        return [value[-1][0], value[-2][0]]

        