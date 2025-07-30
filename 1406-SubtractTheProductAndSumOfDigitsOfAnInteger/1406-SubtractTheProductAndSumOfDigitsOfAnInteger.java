// Last updated: 7/30/2025, 12:23:17 PM
class Solution {
    public int subtractProductAndSum(int n) {
        int sum = 0;
        int product = 1;
        while(n>0){
            sum += n%10;
            product *= n%10;
            n /= 10;
        }
        return product-sum;
    }
}