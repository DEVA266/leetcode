// Last updated: 7/30/2025, 12:23:01 PM
class Solution {
    public int countBalls(int lowLimit, int highLimit) {
        // int[] count = new int[50];
        // for(int i=lowLimit; i<=highLimit; i++){
        //     int sum = digitsum(i);
        //     count[sum]++;
        // }
        // return Arrays.stream(count).max().getAsInt();
        int[] count = new int[50];
        for(int i=lowLimit; i<=highLimit; i++){
            int sum = digitsum(i);
            count[sum]++;
        }
        int max = 0;
        for(int c : count){
            if(c>max){
                max = c;
            }
        }
        return max;

    }
    private int digitsum(int i){
        int sum = 0;
        while(i!=0){
            sum += i%10;
            i /= 10;
        }
        return sum;
    }
}