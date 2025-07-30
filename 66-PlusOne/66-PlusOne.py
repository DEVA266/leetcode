# Last updated: 7/30/2025, 12:24:49 PM
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for i in digits:
            num += str(i)
        num = int(num)+1
        ans = [ int(i) for i in str(num)]
        return ans
