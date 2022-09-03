class Solution {
    public int removeElement(int[] nums, int val) {
        int res=0;
        int dIndex = 0;
        int i=0;
        int element;
        for(i=0;i<nums.length ;i++){
            element = nums[i];
            if(element!=val){
                res++;
                nums[dIndex] = element;
                dIndex++;
            }
        }
        return res;
    }
}