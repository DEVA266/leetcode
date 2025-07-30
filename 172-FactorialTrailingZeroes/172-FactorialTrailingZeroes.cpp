// Last updated: 7/30/2025, 12:24:28 PM
class Solution {
public:
    int trailingZeroes(int n) {
        int c = 0,temp = n;
        while (temp>4){
            temp/=5;
            c+=temp;
        }
        return c;
    }
};