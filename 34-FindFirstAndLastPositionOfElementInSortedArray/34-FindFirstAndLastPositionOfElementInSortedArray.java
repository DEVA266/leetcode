// Last updated: 7/30/2025, 12:24:58 PM
class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] result = {-1,-1};
        int first = indexFinder(nums,target,true);
        int last = indexFinder(nums,target,false);
        result[0] = first;
        result[1] = last;

        return result;     
    }

    public int indexFinder(int[] nums, int target, boolean searching){
        int start = 0;
        int end = nums.length-1;
        int mid = 0;
        int index = -1;
        while(start<=end){
            mid = start + (end-start)/2;
            
            if(nums[mid] < target){
                start = mid + 1;
            }
            else if (nums[mid] > target){
                end = mid - 1;
            }
            else{
                index = mid;
                if(searching){
                    end = mid - 1;
                }
                else{
                    start = mid + 1;
                }
            }

        }
        return index;
    }
}