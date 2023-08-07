class Solution {
    public int[] compute(int n,int column){
        int y = n%column;
        int x = 0;
        // int v = 0;
        while (n>=column){
            n-=column;
            x+=1;
        }
        return new int[]{x,y};
    }
    public boolean searchMatrix(int[][] mat, int key) {
        int column = mat[0].length;
        int low = 0;
        int high = mat.length*column - 1;
        int mid,x,y;
        while(low<=high){
            mid = (low+high)/2;
            int[] v = compute(mid,column);
            x = v[0];
            y = v[1];
            if (mat[x][y]==key){
                return true;
            }
            else if(mat[x][y]>key){
                high = mid-1;
            }
            else{
                low = mid+1;
            }
        }
        return false;
        
    }
}