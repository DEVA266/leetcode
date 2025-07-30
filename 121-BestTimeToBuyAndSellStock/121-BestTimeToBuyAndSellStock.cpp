// Last updated: 7/30/2025, 12:24:45 PM
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int bestbuy=prices[0];
        int maxProfit=0;
        for(int i=1 ; i<prices.size() ;i++){
            maxProfit = max( prices[i] - bestbuy, maxProfit);
            bestbuy = min(bestbuy,prices[i]);
        }
        return maxProfit;
    }
};