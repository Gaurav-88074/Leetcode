class Solution {
    public int LCS(int m,int n,int[] nums1, int[] nums2,int[][] dp){
        if(m==-1 ||n==-1){
            return 0;
        }
        if(dp[m][n]!=-1){
            return dp[m][n];
        }
        if(nums1[m] == nums2[n]){
            dp[m][n] = 1+ LCS(m-1,n-1,nums1,nums2,dp);
        }
        else{
            int left  = LCS(m-1,n,nums1,nums2,dp);
            int right = LCS(m,n-1,nums1,nums2,dp);
            dp[m][n]  = Math.max(left,right);
        }
        return dp[m][n];
    }
    public int maxUncrossedLines(int[] nums1, int[] nums2) {
        int m = nums1.length;
        int n = nums2.length;
        
        
        int[][] dp = new int[m][n];
        for(int[] arr : dp){
            Arrays.fill(arr,-1);
        }
        int lcs = LCS(m-1,n-1,nums1,nums2,dp);
        return lcs;
    }
}