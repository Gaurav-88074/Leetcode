class Solution {
    public int LCS(int m,int n,String word1,String word2,int[][] dp){
        if(m==-1 ||n==-1){
            return 0;
        }
        if(dp[m][n]!=-1){
            return dp[m][n];
        }
        if(word1.charAt(m) == word2.charAt(n)){
            dp[m][n] = 1+ LCS(m-1,n-1,word1,word2,dp);
        }
        else{
            int left  = LCS(m-1,n,word1,word2,dp);
            int right = LCS(m,n-1,word1,word2,dp);
            dp[m][n]  = Math.max(left,right);
        }
        return dp[m][n];
    }
//     public int longestPalindromeSubseq(String s) {
//         String word1 = s;
//         StringBuilder sb=new StringBuilder(s);  
//         sb.reverse();  
//         String word2 = sb.toString();
//         int m = word1.length();
//         int n = word2.length();
        
        
//         int[][] dp = new int[m][n];
//         for(int[] arr : dp){
//             Arrays.fill(arr,-1);
//         }
//         int lcs = LCS(m-1,n-1,word1,word2,dp);
//         return lcs;
    public int longestCommonSubsequence(String word1, String word2) {
        int m = word1.length();
        int n = word2.length();
        
        
        int[][] dp = new int[m][n];
        for(int[] arr : dp){
            Arrays.fill(arr,-1);
        }
        int lcs = LCS(m-1,n-1,word1,word2,dp);
        return lcs;
    }
}