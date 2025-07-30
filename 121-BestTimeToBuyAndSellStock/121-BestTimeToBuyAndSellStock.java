// Last updated: 7/30/2025, 12:24:40 PM
class Solution {
    public int maxProfit(int[] prices) {
        int mi = prices[0];
        int profit=0;
        for(int p : prices){
            mi = Math.min(mi,p);
            profit = Math.max(profit,p-mi);
        }
        return profit;
        // for(int i = 1; i<prices.length; i++){
            
        // }
    }
}