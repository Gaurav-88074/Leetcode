class Solution {
    public int compute(int[][] grid,int index,int row){
        if(row==grid.length){
            return index;
        }
        if(grid[row][index]==1 && (index+1==grid[0].length || grid[row][index+1]==-1)){
            return -1;
        }
        else if(grid[row][index]==-1 && (index-1 == -1 || grid[row][index-1]==1)){
            return -1;
        }
        else if(grid[row][index]==1){
            return compute(grid,index+1,row+1);
        }
        else{
            return compute(grid,index-1,row+1);
        }
        
    }
    public int[] findBall(int[][] grid) {
        int size = grid[0].length;
        int[] res = new int[size];
        // int pre=-1;
        for(int i = 0 ; i<grid[0].length ; i++){
            res[i] = compute(grid,i,0);
        }
        return res;
    }
}