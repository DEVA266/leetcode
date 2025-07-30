// Last updated: 7/30/2025, 12:22:53 PM
class Solution {
    public int findGCD(int[] nums) {
        int min = Arrays.stream(nums).min().getAsInt();
        int max = Arrays.stream(nums).max().getAsInt();
        while(min!=0){
            int temp = max % min;
            max = min;
            min = temp;
        }
        return max;
    }
}