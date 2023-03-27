class Solution {
    public int compute(int[][] grid,int x,int y,Integer[][] dp){
        // if( (x>=grid.length && y!=grid[0].length) || 
        //     (x!=grid.length && y>=grid[0].length)){
        //     return 1;
        // }
        if(dp[x][y]!=null){
            return dp[x][y];
        }
        if(x>=grid.length || y>=grid[0].length){
            return 1000;
        }
        if(x==grid.length-1 && y==grid[0].length-1){
             dp[x][y]  = grid[x][y];
             return dp[x][y];
        }
        
        int right  =  grid[x][y] + compute(grid,x+1,y,dp);
        int bottom =  grid[x][y] + compute(grid,x,y+1,dp);
        dp[x][y] = Math.min(right,bottom);
        return dp[x][y];
        
    }
    public int minPathSum(int[][] grid) {
        Integer[][] dp = new Integer[201][201];
        // Arrays.fill(dp,-1);
        // for (int[] row: dp)
        // Arrays.fill(row, -1);
        return compute(grid,0,0,dp);
    }
}