// Last updated: 7/30/2025, 12:23:46 PM
class Solution {
    public String convertToBase7(int num) {
        if(num==0){
            return "0";
        }
        StringBuilder ans = new StringBuilder();
        int temp = Math.abs(num);
        while(temp>0){
            ans.append(temp%7 + "");
            temp /= 7;
        }
        if(num<0){
            ans.append("-");
        }
        return ans.reverse().toString();
    }
}