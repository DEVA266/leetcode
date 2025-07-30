# Last updated: 7/30/2025, 12:23:15 PM
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)) :
                if nums[j] < nums[i] :
                    count += 1
            ans.append(count)
        return ans
            

        
