// Last updated: 7/31/2025, 2:04:03 PM
class Solution {
    public int[][] flipAndInvertImage(int[][] image) {
        int[][] ans = new int[image.length][image.length];
        for(int row=0; row<image.length; row++){
            int n = image[row].length;
            for(int i=0; i<n; i++){
                if(image[row][n-i-1] == 0) ans[row][i] = 1;
                else ans[row][i] = 0;
            }
        }
        return ans;
    }
}