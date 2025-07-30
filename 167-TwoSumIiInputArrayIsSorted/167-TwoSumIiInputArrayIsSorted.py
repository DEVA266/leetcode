# Last updated: 7/30/2025, 12:24:30 PM
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        m = {}
        for i in range(len(numbers)):
            if target-numbers[i] in m :
                return [m[target-numbers[i]], i+1]
            else :
                m[numbers[i]] = i+1

        