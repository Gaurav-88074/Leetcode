class Solution {
    public int fibo(int n,int[] dp){
        if(dp[n]!=-1){
            return dp[n];
        }
        if(n==0 || n==1){
            return n;
        }
        dp[n] = fibo(n-1,dp) + fibo(n-2,dp);
        return dp[n];
    }
    public int climbStairs(int n) {
        int[] dp = new int[n+2];
        Arrays.fill(dp,-1);
        return fibo(n+1,dp);
    }
}
/*
0
1
2
3
5
8
//------------
n = 4
1 1 1 1
1 2 1
2 1 1 
1 1 2
2 2
//--------------
n=5
1 1 1 1 1
1 2 1 1
2 1 1 1
1 2 1 1
1 1 2 1
1 1 1 2
1 2 2
2 2 1

*/