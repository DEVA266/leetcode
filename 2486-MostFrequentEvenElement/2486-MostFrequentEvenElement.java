// Last updated: 7/30/2025, 12:22:45 PM
class Solution {
    public int mostFrequentEven(int[] nums) {
        HashMap<Integer,Integer> m = new HashMap<>();
        int value = 1000000;
        int frequency = 0;
        for (int i : nums){
            if(i%2==0){
                int count = m.getOrDefault(i,0) + 1;
                m.put(i,count);
                if( count>frequency || count==frequency && i<value){
                    value = i;
                    frequency = count ;
                }
            }
        }
        if(frequency == 0){
            return -1;
        }
        else {
            return value;
        }
    }
}