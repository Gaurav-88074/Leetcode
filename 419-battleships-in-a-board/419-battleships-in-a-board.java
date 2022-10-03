class Solution {
    int res = 0;
    public void go(char[][] board,int x,int y){
        if(x==board.length || y==board[0].length || board[x][y]=='.'){
            return;
        }
        
        go(board,x+1,y);
        go(board,x,y+1);
        board[x][y]='.';
        
    }
    public int countBattleships(char[][] board) {
        for(int i = 0 ; i<board.length ; i++){
            for(int j = 0 ; j<board[0].length ; j++){
                if(board[i][j]=='X'){
                    res+=1;
                    go(board,i,j);
                }
            }
        }
        return res;
    }
}