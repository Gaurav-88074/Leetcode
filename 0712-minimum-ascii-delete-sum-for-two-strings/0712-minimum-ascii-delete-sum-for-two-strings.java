class Solution {
    public int LCS(int m,int n,String word1,String word2,int[][] dp){
        if(m==-1 ||n==-1){
            return 0;
        }
        if(dp[m][n]!=-1){
            return dp[m][n];
        }
        if(word1.charAt(m) == word2.charAt(n)){
            dp[m][n] = word1.charAt(m) + LCS(m-1,n-1,word1,word2,dp);
        }
        else{
            int left  = LCS(m-1,n,word1,word2,dp);
            int right = LCS(m,n-1,word1,word2,dp);
            dp[m][n]  = Math.max(left,right);
        }
        return dp[m][n];
    }
    public int minimumDeleteSum(String s1, String s2) {
        int m = s1.length();
        int n = s2.length();
        
        //-----------------------------
        int[][] dp = new int[m][n];
        for(int[] arr : dp){
            Arrays.fill(arr,-1);
        }
        int lcs = LCS(m-1,n-1,s1,s2,dp);
        //------------------------------
        // System.out.println(lcs);
        int sum= 0;
        for(int i=0 ; i<s1.length() ; i++){
            sum+=s1.charAt(i);
        }
        for(int i=0 ; i<s2.length() ; i++){
            sum+=s2.charAt(i);
        }
        //------------------------------
        return sum-(2*lcs);
    }
}