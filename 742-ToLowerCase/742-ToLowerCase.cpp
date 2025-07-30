// Last updated: 7/30/2025, 12:23:39 PM
class Solution {
public:
    string toLowerCase(string s) {
        string ans="";
        for(char c:s){
            if (c>64 && c<91)
            ans+=c+32;
            else
            ans+=c;
        }
        return ans;
    }
};