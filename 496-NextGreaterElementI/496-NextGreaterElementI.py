# Last updated: 7/30/2025, 12:23:49 PM
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums1)):
            done = True
            for j in range(nums2.index(nums1[i]),len(nums2)):
                if nums2[j] > nums1[i]:
                    ans.append(nums2[j])
                    done = False
                    break
            if(done):
                ans.append(-1)
        return ans
            

        