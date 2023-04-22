class Solution {
    public int compute(List<List<Integer>> triangle,Integer[][] dp,int index,int row){
    
        if(row==triangle.size()){
            return 0;
        }
        //---------------------
        if(dp[row][index]!=null){
            return dp[row][index];
        }
        //--------------------------
        int left  = triangle.get(row).get(index) +  compute(triangle,dp,index ,row + 1);
        
        // if(row+1 < triangle.size()){
        //     dp[row+1][index] = left;
        // }
        //---------------------------
        int right = triangle.get(row).get(index) +  compute(triangle,dp,index+1,row + 1);
        
        // if(row+1 < triangle.size() && index+1< triangle.get(row+1).size()){
        //     dp[row+1][index+1] = right;
        // }
        
        //---------------------------------
        dp[row][index] =  Math.min(left,right);
        //------------------------------------
        return dp[row][index];
    }
    public int minimumTotal(List<List<Integer>> triangle) {
        int n = triangle.size();
        Integer[][] dp = new Integer[n][];
        
        for(int i = 0 ; i<n ; i++){
            dp[i] = new Integer[triangle.get(i).size()];
        //     Arrays.fill(dp[i],-1);
        }
        // Arrays.fill(dp,-1);
        return compute(triangle,dp,0,0);
    }
}