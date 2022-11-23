class Solution {
    public boolean check(char[][] board){
        HashSet<Character> set = new HashSet<>();
        boolean p;
        //-------------------------------
        for(int i = 0 ; i<9 ; i++){
            set.clear();
            for(int j = 0 ; j<9 ;j++){
                if(board[i][j]=='.')continue;
                p = set.add(board[i][j]);
                if(!p)return p;
            }
        }
        for(int i = 0 ; i<9 ; i++){
            set.clear();
            for(int j = 0 ; j<9 ;j++){
                if(board[j][i]=='.')continue;
                p = set.add(board[j][i]);
                if(!p)return p;
            }
        }
        //----------------------------------------
        for(int i = 0 ; i<9 ;i+=3){
            for(int j = 0; j<9; j+=3){
                set.clear();
                
                for(int k =i ; k<(i+3) ; k++){
                    for(int l = j ; l<(j+3) ; l++){
                        // System.out.print(k+""+l+" ");
                        if(board[k][l]=='.')continue;
                        p = set.add(board[k][l]);
                        if(!p)return p;
                    }
                    // System.out.println();
                }
                // System.out.println();
            }
            // System.out.println();
        }
        
        return true;
    }
    public boolean isValidSudoku(char[][] board) {
        
        
        return check(board);
    }
}