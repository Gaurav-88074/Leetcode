class Solution {
    public int[][] rangeAddQueries(int n, int[][] queries) {
        int[][] mat = new int[n][n];
        //brute force
        //wtf
        for (int[] query : queries) {
            int x1 = query[0], y1 = query[1], x2 = query[2], y2 = query[3];
            for (int i = x1; i <= x2; i++) {
                mat[i][y1]+=1;
                
                if (y2+1<n) mat[i][y2+1]-=1;
            }   
        }
        for(int i = 0; i < n; i++){
            int v=0;
            for(int j = 0; j < n; j++){
                
                v+=mat[i][j];
                mat[i][j]=v;
            }
        }
            
        return mat;
    }
}