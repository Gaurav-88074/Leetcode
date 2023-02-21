class Solution {
    public int singleNonDuplicate(int[] nums) {
        // [1,1,2,3,3,4,4,8,8]
        // [0,1,2,3,4,5,6,7,8]
        int low = 0;
        int high=nums.length - 1;
        int mid;
        int elements;
        while(low<=high){
            mid = low + ((high-low)/2);
            elements = mid + 1;
            if(elements%2==0){
                if(mid-1>=0 && nums[mid-1]!=nums[mid]){
                    high = mid - 1;
                }
                else{
                    low  = mid + 1;
                }
            }
            else{
                // System.out.println("odd case hit "+mid);
                if(mid-1>=0 && nums[mid-1]==nums[mid]){
                    high = mid - 1;
                    // System.out.println("Going towards left "+low+" "+high);
                }
                else{
                    low  = mid + 1;
                    // System.out.println("Going towards right "+low+" "+high);
                }
            }
        }
        return nums[high];
    }
}