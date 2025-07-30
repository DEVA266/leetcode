// Last updated: 7/30/2025, 12:47:00 PM
class Solution {
    public int maximumWealth(int[][] accounts) {
        int max = Integer.MIN_VALUE;
        for(int i=0; i<accounts.length; i++){
            int sum = 0;
            for(int j=0; j<accounts[i].length; j++){
                sum += accounts[i][j];
            }
            if(sum>=max){
                max = sum;
            }
        }
        return max;
    }
}