# Last updated: 7/30/2025, 12:22:39 PM
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        nums = sorted(nums,reverse=True)
        ans = {}
        for i in nums:
            if i%2==0:
                if i in ans:
                    ans[i] += 1
                else :
                    ans[i] = 1
        m = 0
        res = -1
        for k,v in ans.items():
            if m <= v :
                m = v
                res = k
        return res

        