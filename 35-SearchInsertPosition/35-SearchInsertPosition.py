# Last updated: 7/30/2025, 12:24:56 PM
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        mid = 0
        while start <= end :
            mid = (start + end )//2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                start = mid + 1
            else :
                end = mid - 1
        return start