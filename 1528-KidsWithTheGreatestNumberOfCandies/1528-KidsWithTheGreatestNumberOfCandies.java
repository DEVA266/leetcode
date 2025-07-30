// Last updated: 7/30/2025, 1:02:14 PM
class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int max = Integer.MIN_VALUE;
        for(int i=0; i<candies.length; i++){
            if(candies[i] > max){
                max = candies[i];
            }
        }
        List<Boolean> ans = new ArrayList<>();
        for(int i=0; i<candies.length; i++){
            ans.add(candies[i]+extraCandies >= max);
        }
        return ans;
    }
}