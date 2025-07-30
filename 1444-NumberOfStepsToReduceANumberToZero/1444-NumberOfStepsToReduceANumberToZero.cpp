// Last updated: 7/30/2025, 12:23:30 PM
class Solution {
public:
    int numberOfSteps(int num) {
        int count=0;
        while(num!=0){
            if(num%2==0){
                num /=2;
                count++;
            }
            else{
                num--;
                count++;
            }
        }
        return count;
    }
};