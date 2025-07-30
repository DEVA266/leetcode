// Last updated: 7/30/2025, 11:57:00 AM
class Solution {
    public int maxSum(int[] nums) {
        Arrays.sort(nums);
        if(nums[nums.length -1] < 0){
            return nums[nums.length -1];
        }
        Set<Integer> n = new HashSet<>();
        int sum = 0;
        for(int i=0; i<nums.length; i++){
            if(!(n.contains(nums[i])) && nums[i]>0){
                n.add(nums[i]);
                sum += nums[i];
            }
        }
        return sum;
    }
}