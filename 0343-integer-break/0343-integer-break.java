class Solution {
    private Integer[] dp ;
    public int compute(int num){
        if(num<=2){
            return 1;
        }
        if(dp[num]!=null) return dp[num];
        int res =1;
        for(int i = 1 ; i<num ; i++){
            int v1 = compute(i);
            int v2 = compute(num-i);
            res = Math.max(res,v1*v2);
            res = Math.max(res,i*(num-i));
            res = Math.max(res,v1*(num-i));
            res = Math.max(res,v2*i);
        }
        dp[num] = res;
        return res;
    }
    public int integerBreak(int n) {
        dp = new Integer[n+1];
        int res = compute(n);
        return res;
    }
}