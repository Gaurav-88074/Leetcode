class Solution {
    private int mv = 100000;
    int[] dp = new int[10001];
    public int compute(int[] nums,int index){
        if(index>=nums.length){
            return this.mv;
        }
        if(index==nums.length-1){
            return 0;
        }
        if(dp[index]!=-1){
            return dp[index];
        }
        int value = nums[index];
        int minSteps = this.mv;
        int v;
        for(int i=1 ; i<=value ; i++){
            v = 1 + compute(nums,index+i);
            // if(index+i<nums.length){
            //     dp[index+i] = v;
            // }
            minSteps = Math.min(minSteps,v);
        }
        dp[index] = minSteps;
        return minSteps;
    }
    public int jump(int[] nums) {
        
        Arrays.fill(dp,-1);
        return compute(nums,0);
    }
}