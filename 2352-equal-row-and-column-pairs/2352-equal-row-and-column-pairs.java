class Solution {
    public int equalPairs(int[][] grid) {
        int res = 0;
        for(int i = 0 ;i<grid.length ; i++){
            for(int j = 0;j<grid.length ;j++){
                boolean check = true;
                for(int k = 0 ;k<grid.length ;k++){
                    if(grid[i][k]!=grid[k][j]){
                        check=false;
                        break;
                    }
                }
                if(check==true) res+=1;
            }
        }
        return res;
    }
}