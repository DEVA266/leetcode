// Last updated: 7/30/2025, 12:23:55 PM
class Solution {
    public int thirdMax(int[] nums) {
        Set<Integer> value = new HashSet<>();
        for(int n : nums){
            value.add(n);
        }
        if(value.size()<3){
            return Collections.max(value);
        }
        value.remove(Collections.max(value));
        value.remove(Collections.max(value));
        return Collections.max(value);
    }
}