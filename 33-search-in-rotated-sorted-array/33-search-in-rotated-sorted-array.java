class Solution {
    public int Pivot(int[] nums,int start,int end){
        int mid;
        while(start<=end){
            // System.out.println(start+" - "+end);
            mid = (start+end)/2;
            // System.out.println("mid : "+mid+" , value : "+nums[mid]);
            // if(mid==0 || mid==nums.length-1){
            //     return mid;
            // }
            if(mid-1 >-1 && mid+1<nums.length && 
               nums[mid]>nums[mid+1] && nums[mid]>nums[mid-1]){
                return mid;
            }
            else if(mid-1 > -1 && (nums[mid-1]>nums[mid] ||nums[start]>nums[mid]) ){
                // System.out.println("Going to left");
                end = mid-1;
            }
            else if(mid+1 < nums.length && (nums[mid]<nums[mid+1]||nums[end]>nums[mid])){
                // System.out.println("Going to right");
                start = mid+1;
            }
            else if(mid==0 || mid==nums.length-1){
                return mid;
            }
        }
        return -1;
    }
    public int binarySearch(int[] nums,int start,int end,int target){
        int mid;
        while(start<=end){
            mid = (start+end)/2;
            if (nums[mid] == target) {
                return mid;
            } 
            else if(target < nums[mid]) {
                end -=1;
            }
            else{
                start+=1;
            }
        }
        return -1;
    }
    public int search(int[] nums, int target) {
        int res = Pivot(nums,0,nums.length-1);
        if (nums[res]==target) {
            return res;
        }
        int left = binarySearch(nums,0,res-1,target);
        int right = binarySearch(nums,res+1,nums.length-1,target);
        
        if(left!=-1){
            return left;
        }
        return right;
    }
}