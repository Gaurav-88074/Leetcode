class Solution {
    public void transpose(int[][] matrix){
        int temp;
        for(int i = 0 ;i < matrix.length ; i++){
            for(int j=i ; j<matrix.length ; j++){
                temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
    }
    public void reverse(int[] row){
        int low = 0;
        int high = row.length - 1;
        int temp;
        while(low<high){
            temp = row[low];
            row[low]  = row[high];
            row[high] = temp;
            low++;
            high--;
        }
    }
    public void rotate(int[][] matrix) {
        transpose(matrix);
        for(int[] row : matrix){
            reverse(row);
        }
    }
}
/*
[1,2,3] [1,4,7] [7,4,1]
[4,5,6] [2,5,8] [8,5,2]
[7,8,9] [3,6,9] [9,6,3]
*/