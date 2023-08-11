class Solution {
    // public List<Integer> l = new ArrayList<>();
    public int[][] dp;
    public int compute(int amount,int[] coins,int index){
        if(amount==0){
            // System.out.println(l.toString());
            return 1;
        }
        if(amount<0 || index==coins.length){
            return -1;
        }
        //-------------------------
        if(dp[amount][index]!=-1){
            return dp[amount][index];
        }
        //-------------------------
        int value;
        int res = 0;
        for(int i = index ; i>=0 ; i--){
            // l.add(coins[i]);
            value = compute(amount - coins[i],coins,i);
            if(value!=-1){
                res +=value;
            }
            // l.remove(l.size()-1);
        }
        dp[amount][index] = res;
        return res;
    }
    public int change(int amount, int[] coins) {
        // Arrays.sort(coins);//array is alredy sorted bro
        // reverse(coins);//we are avoind it now 
        // System.out.println(Arrays.toString(coins));
        this.dp = new int[amount+1][coins.length];
        for(int[] row : dp){
            Arrays.fill(row,-1);
        }
        
        // int res = compute(amount,coins,0);
        int res = compute(amount,coins,coins.length-1);
        return res;
    }
    // public void reverse(int a[]){
    //     int low  = 0;
    //     int high = a.length-1;
    //     int temp;
    //     while(low<high){
    //         temp = a[low];
    //         a[low] = a[high];
    //         a[high] = temp;
    //         low++;
    //         high--;
    //     }
    // }
}