class Solution {
    public int[] findErrorNums(int[] nums) {
        int a=-1,b=-1;
        boolean[] ad = new boolean[nums.length+1];
        for(int i=0 ; i<nums.length ; i++){
            if(ad[nums[i]]==true){
                a = nums[i];
                // break;
            }
            
            ad[nums[i]] = true;
        }
        for(int i=1 ; i<=nums.length ; i++){
            if(ad[i]==false){
                b = i;
                break;
            }
            // ad[nums[i]] = 1;
        }
        return new int[]{a,b};
    }
}