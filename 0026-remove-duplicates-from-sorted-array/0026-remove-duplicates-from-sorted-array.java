class Solution {
    public int removeDuplicates(int[] nums) {
        if(nums.length ==0){
            return 0;
        }
        int pre = nums[0];
        int dIndex = 0;
        int res = 1;
        int i;
        for(i=1;i<nums.length ; i++){
            if(nums[i]!=pre){
                dIndex++;
                nums[dIndex] = nums[i];
                res+=1;
                pre = nums[i];
            }
            else{
                continue;
            }
        }
        return res;
    }
}