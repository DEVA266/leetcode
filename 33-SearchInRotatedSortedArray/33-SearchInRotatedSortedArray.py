# Last updated: 7/30/2025, 12:24:59 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0,len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left]<= target < nums[mid]:
                    right = mid-1
                else :
                    left = mid+1
            else :
                if nums[mid] < target <= nums[right]:
                    left = mid+1
                else :
                    right = mid-1
        return -1