class Solution {
    public int minCoin(int[] coins,int amount,Integer[] dp){
        
        if(amount<0){
            return Integer.MAX_VALUE;
            // return -1;
        }
        if(amount==0){
            return 0;
        }
        if(dp[amount]!=null){
            return dp[amount];
        }
        int min = Integer.MAX_VALUE;
        int value;
        for(int i = 0 ; i<coins.length ; i++){
            value = minCoin(coins,amount-coins[i],dp);
            // if(amount-coins[i]>-1)
            //     dp[amount-coins[i]] = value;
            if(value!=Integer.MAX_VALUE){
                min = Math.min(min,1 + value);
            }
        }
        dp[amount] = min;
        return dp[amount];
    }
    public int coinChange(int[] coins, int amount) {
        Integer[] dp = new Integer[amount+1];
        // Arrays.fill(dp,-1);
        int res =  minCoin(coins,amount,dp);
        if(res==Integer.MAX_VALUE)
            return -1;
        return res;
    }
    public int numSquares(int n) {

        int v=1;
        List<Integer> value = new ArrayList<>();
        while(v*v<=n){
            value.add(v*v);
            v+=1;
        }
        int[] values = value.stream().mapToInt(i -> i).toArray();
         // System.out.println(Arrays.toString(values));
        
        return coinChange(values,n);
    }
}