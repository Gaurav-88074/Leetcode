class Solution {
    public boolean isPossible = false;
    public int res = 0;
    public void compute(int[][] grid1, int[][] grid2,int x,int y){
        if(x==grid1.length || x==-1 || y==grid1[0].length || y==-1||grid2[x][y]==0){
            return;
        }
        if(grid1[x][y] == 0){
            isPossible = false;
            // return;
        }
        grid2[x][y]=0;
        
        compute(grid1,grid2,x,y+1);
        compute(grid1,grid2,x,y-1);
        compute(grid1,grid2,x+1,y);
        compute(grid1,grid2,x-1,y);
        
        
    }
    public int countSubIslands(int[][] grid1, int[][] grid2) {
        for(int i = 0 ;i<grid1.length ; i++){
            for(int j = 0 ;j<grid1[0].length ; j++){
                if(grid1[i][j]==1 && grid2[i][j]==1){
                    // System.out.println(i+ " : "+j);
                    isPossible = true;
                    compute(grid1,grid2,i,j);
                    if(isPossible){
                        res+=1;
                    }
                }
            }
        }
        return res;
    }
}