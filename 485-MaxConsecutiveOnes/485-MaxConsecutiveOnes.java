// Last updated: 7/30/2025, 12:23:52 PM
class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int count = 0;
        int max = 0;
        for(int i : nums){
            if(i==1){
                count ++;
                if(count > max){
                    max = count;
                }
            }
            else{
                count = 0;
            }
        }
        return max;
    }
}