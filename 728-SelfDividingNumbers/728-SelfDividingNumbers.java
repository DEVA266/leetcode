// Last updated: 7/30/2025, 12:23:42 PM
class Solution {
    public List<Integer> selfDividingNumbers(int left, int right) {
        List<Integer> nums = new ArrayList<>();
        for(int i=left; i<=right; i++){
            boolean ans = true;
            int temp = i;
            while(temp>0){
                if(temp%10 == 0 || i%(temp%10)!=0){
                    ans = false;
                    break;
                }
                temp /= 10;
            }
            if(ans){
                nums.add(i);
            }
        }
        return nums;
    }
}