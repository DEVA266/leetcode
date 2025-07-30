// Last updated: 7/30/2025, 12:23:22 PM
class Solution {
    public String gcdOfStrings(String str1, String str2) {
        if (!(str1+str2).equals(str2+str1)){
            return "";
        }
        int len = gcd(str1.length(),str2.length());
        return str1.substring(0,len);
    }
    public int gcd(int len1, int len2){
        while(len2 != 0){
            int temp = len1 % len2;
        len1 = len2;
        len2 = temp;
        }
        return len1;
    }
}