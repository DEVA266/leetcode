// Last updated: 7/30/2025, 12:22:54 PM
class Solution {
    public boolean isThree(int n) {
        int count = 0;
        for(int i=1; i<=Math.abs(n); i++){
            if(n%i==0) count++;
            if(count>3) return false;
        }
        return (count==3);
    }
}