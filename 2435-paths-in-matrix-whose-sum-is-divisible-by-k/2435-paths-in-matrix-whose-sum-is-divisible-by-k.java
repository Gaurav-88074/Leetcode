class Solution {
    public Integer[][][] dp;
    int[][] grid;
    int mod = 1000000007;
    int k ;
    public int compute(int x,int y,int s){
        if(x==grid.length-1 && y==grid[0].length-1){
            s+=grid[x][y];
            if (s%k==0)
                return 1;
            return 0;
        }
                
        if (x==grid.length || y==grid[0].length){
            return 0;
        }
        s+=grid[x][y];
        s%=k;
        if (dp[x][y][s]!=null) return dp[x][y][s];

        int right = compute(x,y+1,s);
        int down = compute(x+1,y,s);

        long r  = (long)(right + down);
        r%=(long)mod;
        
        dp[x][y][s] = (int)r;
        return (int)r;
            
    }
    public int numberOfPaths(int[][] grid, int k) {
        this.grid = grid;
        this.k = k;
        dp =new Integer[grid.length][grid[0].length][k];
        return compute(0,0,0)%mod;
        
    }
}