class Solution {
    public int arraySign(int[] nums) {
        int n=0;
        for (int i: nums){
            if(i==0){
                return 0;
            }
            else if(i<0){
                n+=1;
            }
        }
        if((n&1)==1){
            return -1;
        }
        return 1;
        
    }
}