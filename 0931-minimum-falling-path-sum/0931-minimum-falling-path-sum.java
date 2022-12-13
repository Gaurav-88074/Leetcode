class Solution {
    private Integer[][] dp;
    public int compute(int[][] matrix,int row,int column){
        if(column==-1 || column==matrix[0].length){
            return Integer.MAX_VALUE;
        }
        if(row==matrix.length){
            return 0;
        }
        if(dp[row][column]!=null) return dp[row][column];
        
        int res = Integer.MAX_VALUE;
        
        int left  = compute(matrix, row+1, column - 1);
        res = (left!=Integer.MAX_VALUE) ?  Math.min(res,left+matrix[row][column]) : res;
        
        int head  = compute(matrix, row+1, column + 0);
        res = (head!=Integer.MAX_VALUE) ?  Math.min(res,head+matrix[row][column]) : res;
        
        int right = compute(matrix, row+1, column + 1);
        res = (right!=Integer.MAX_VALUE) ?  Math.min(res,right+matrix[row][column]) : res;
        // System.out.println(res+" , "+column);
        
        dp[row][column] = res;
        
        return res;
        
        
        
        
    }
    public int minFallingPathSum(int[][] matrix) {
        int rows    = matrix.length;
        int columns = matrix[0].length;
        dp = new Integer[rows][columns];
        
        int res = Integer.MAX_VALUE;
        for(int i = 0;i<columns ; i++){
            int ans = compute(matrix,0,i);
            res = Math.min(res,ans);
        }
        return res;
    }
}