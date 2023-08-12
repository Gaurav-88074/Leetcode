class Solution {
    private int rows;
    private int column;
    private int res = 0;
    private List<String> debug = new ArrayList<>();
    public int path(int[][] matrix,int m, int n,int dp[][]) {
        
        if(m<0 || n<0){
            return 0;
        }
        if(dp[m][n]!=-1){
            return dp[m][n];
        }
        if(matrix[m][n]==1){
            return 0;
        }
        if(m==0 && n==0){
            return 1;
        }
        
        int top  = path(matrix,m-1,n,dp);
        int left = path(matrix,m,n-1,dp);
        if(m-1>=0){
            dp[m-1][n] = top;
        }
        if(n-1>=0){
            dp[m][n-1] = left;
        }
        dp[m][n] = top + left;
        return dp[m][n];
    }
    //----------------------------------------------------------
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        this.rows   = obstacleGrid.length;
        this.column = obstacleGrid[0].length;
        int[][] dp = new int[rows][column];
        for(int[] i : dp){
            Arrays.fill(i,-1);
        }
        return path(obstacleGrid,rows-1,column-1,dp);
    }
}