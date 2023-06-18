class Solution {
    private Integer[][] dp;
    private int mod = 1000000007;
    public int count(int[][] matrix,int m,int n,int prev){
        if(n==-1 || m==-1 ||
           m == matrix.length  ||
           n==matrix[0].length ||
           matrix[m][n]<=prev  ||
           matrix[m][n]<0){
            return -1;
        }
        //-----------------------
        if(dp[m][n]!=null) return dp[m][n];
        //-----------------------
        //-----------------------
        int v = matrix[m][n];
        matrix[m][n] ^=-5;
        int left  = count(matrix,m,n-1,v);
        if(left!=-1){
            left+=1;
        }
        else{
            left=0;
        }
        int right = count(matrix,m,n+1,v);
        if(right!=-1){
            right+=1;
        }
        else{
            right=0;
        }
        int top   = count(matrix,m+1,n,v);
        if(top!=-1){
            top+=1;
        }
        else{
            top=0;
        }
        int down  = count(matrix,m-1,n,v);
        if(down!=-1){
            down+=1;
        }
        else{
            down=0;
        }
        matrix[m][n] ^=-5;
        //------------------------
        int res = (left+right+top+down)%mod;
        // System.out.println(max);
        
        dp[m][n] = res;
        return res;
        
        
    } 
    
    public int countPaths(int[][] matrix) {
        int res = 0;
        dp = new Integer[matrix.length][matrix[0].length];
        
        for(int i = 0; i<matrix.length ;i++){
            for(int j = 0;j<matrix[0].length;j++){
                int value = count(matrix,i,j,0);
                // System.out.println(value);
                res = (res+value)%mod;
                
            }
        }
        return (res + (matrix.length * matrix[0].length)%mod)%mod;
    }
}