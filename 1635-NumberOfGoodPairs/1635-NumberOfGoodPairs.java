// Last updated: 7/30/2025, 3:38:58 PM
class Solution {
    public int numIdenticalPairs(int[] nums) {
        int goodPair = 0;
        for(int i=0; i<nums.length-1; i++){
            for(int j=i+1; j<nums.length; j++){
                if(nums[i] == nums[j]) goodPair++;
            }
        }
        return goodPair;
    }
}