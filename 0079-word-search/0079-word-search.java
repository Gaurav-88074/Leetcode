class Solution {
    private boolean[][] visited = new boolean[7][7];
    public boolean DFS(char[][] board,String word ,int pos,int m,int n){
        if(pos == word.length()){
            return true;
        }
        if(m==-1 || n==-1||m==board.length || n==board[0].length){
            return false;
        }
        if(visited[m][n]==true){
            return false;
        }
        
        boolean left   = false;
        boolean right  = false;
        boolean top    = false;
        boolean bottom = false;
        visited[m][n] = true;
        if(board[m][n] == word.charAt(pos)){
            left   = DFS(board,word,pos+1,m,n-1);
            right  = DFS(board,word,pos+1,m,n+1);
            top    = DFS(board,word,pos+1,m-1,n);
            bottom = DFS(board,word,pos+1,m+1,n);
        }
        visited[m][n] = false;
        return left || right || top || bottom;
    }
    public boolean exist(char[][] board, String word) {
        // return DFS(board,word,0,0,0);
        for(int i=0 ; i<board.length ; i++){
            for(int j = 0; j<board[0].length ; j++){
                if(DFS(board,word,0,i,j)==true){
                    return true;
                }
            }
        }
        return false;
    }
}