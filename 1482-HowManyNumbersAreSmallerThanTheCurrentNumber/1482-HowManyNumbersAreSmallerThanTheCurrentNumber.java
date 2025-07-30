// Last updated: 7/30/2025, 3:39:08 PM
class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int[] ans = new int[nums.length];

        for(int i=0; i<nums.length; i++){
            ans[i] = counter(nums,nums[i]);
        }
        return ans;
    }

    public int counter(int[] nums, int n){
        int count = 0;
        for(int i=0; i<nums.length; i++){
            if(nums[i] < n) count++;
        }
        return count;
    }
}