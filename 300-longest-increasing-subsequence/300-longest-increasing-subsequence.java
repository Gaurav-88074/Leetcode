class Solution {
    private Integer[][] dp;
    public int compute(int[] nums,int index,int preIndex){
        if(index==nums.length) return 0;
        
        if(dp[index][preIndex+1]!=null) return dp[index][preIndex+1];
        
        int take =0;
        if(preIndex==-1 || nums[index]>nums[preIndex]){
            take = 1 + compute(nums,index+1,index);
//             int skip = compute(nums,index+1,preIndex);
            
//             dp[index][preIndex+1] = Math.max(take,skip);
            
//             return dp[index][preIndex+1];
        }
        
        int skip = compute(nums,index+1,preIndex);
        
        int res = Math.max(take,skip);
        dp[index][preIndex+1] = res;
        
        return res;
    }
    public int lengthOfLIS(int[] nums) {
        dp = new Integer[nums.length+1][nums.length+1];
        return compute(nums,0,-1);
    }
}