class Solution {
    int[][] dp;
    public int longestArithSeqLength(int[] nums) {
        int n = nums.length;
        dp = new int[n][1003];
        for(int[] i: dp){
            Arrays.fill(i, Integer.MIN_VALUE);
        }
        return longestArithSeqLength(nums, 0, -501);
    }

    public int longestArithSeqLength(int[] nums, int curr, int diff) {
        if(curr == nums.length) return 0;

        if(dp[curr][diff + 501] != Integer.MIN_VALUE) return dp[curr][diff + 501];

        int max = 1, op1 = 0;
        if(diff == -501){
            for(int i = curr + 1; i < nums.length; i++){
                max = Math.max(max, Math.max(1 + longestArithSeqLength(nums, i, nums[i] - nums[curr]), longestArithSeqLength(nums, i, diff)));
            }
        }else{
            for(int i = curr + 1; i < nums.length; i++){
                if(nums[i] - nums[curr] == diff){
                    max = Math.max(max, 1 + longestArithSeqLength(nums, i, diff));
                }
            }
        }

        return  dp[curr][diff + 501] = max;
    }
}