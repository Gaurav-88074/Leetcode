class Solution {
    public int nodes = 0;
    public boolean compute(int[][] grid,int x,int y){
        if(x==-1 || y==-1 || x==grid.length||y==grid[0].length){
            return true;
        }
        if(grid[x][y]==0){
            return false;
        }
        nodes+=1;
        grid[x][y] = 0;//had to do so that we won't come again here
        
        boolean left  = compute(grid,x,y-1);
        boolean right = compute(grid,x,y+1);
        boolean top   = compute(grid,x-1,y);
        boolean down  = compute(grid,x+1,y);
        
        
        
        return left||right||top||down;
    }
    public int numEnclaves(int[][] grid) {
        int res =0;
        boolean check;
        for(int i = 0;i<grid.length ; i++){
            for(int j = 0;j<grid[0].length ; j++){
                if(grid[i][j]==1){
                    nodes = 0;
                    check = compute(grid,i,j);
                    if(check==false){
                        res+=nodes;
                    }
                }
            }
        }
        return res;
    }
}