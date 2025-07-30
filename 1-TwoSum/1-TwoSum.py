# Last updated: 7/30/2025, 12:25:10 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for index,value in enumerate(nums):
            if target-value in values.keys():
                return [index,values[target-value]]
            else:
                values[value] = index