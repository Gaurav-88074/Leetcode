class Solution {
    public int compute(int[] nums,int[] dp,int end){
        if(end<0){
            return 0;
        }
        if(end==0){
            return nums[end];
        }
        if(dp[end]!=-1){
            return  dp[end];
        }
        
        int res = 0;
        int next;
        for(int i = end ; i>-1; i--){
            next = compute(nums,dp,i-2);
            // if(i-2 >-1){
            //     dp[i-2] = next;
            // }
            res = Math.max(res,next);
        }
        // int take = compute(nums,dp,end-2);
        // // int skip = compute(nums,dp,end-1);
        
        
        dp[end] =  nums[end] + res;
        return dp[end];
        
    }
    public int rob(int[] nums) {
        int[] dp  = new int[nums.length];
        Arrays.fill(dp,-1);
        
        int end = nums.length-1;
        
        int next     = compute(nums,dp,end);
        int nextNext = compute(nums,dp,end-1);
        return Math.max(next,nextNext);
    }
}