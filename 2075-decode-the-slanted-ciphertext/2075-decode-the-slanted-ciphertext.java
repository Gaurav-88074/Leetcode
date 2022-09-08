class Solution {
    public int getIndex(int cols,int row,int col){
        return cols * row  + col;
    }
    public String decodeCiphertext(String encodedText, int rows) {
        int row = 0;
        int col = 0;
        
        StringBuilder res = new StringBuilder();
        
        int cols = encodedText.length()/rows;
        
        for(int i =0 ; i<cols ; i++){
            row = 0;
            col = i;
            while(row < rows && col < cols){
                res.append(encodedText.charAt(getIndex(cols,row,col)));
                row+=1;
                col+=1;
            }
        }
        // System.out.println(res);
        // System.out.println(res.charAt(res.length()-1)==' ');
        int last = res.length()-1;
        while(last>-1 && res.charAt(last)==' '){
            res.deleteCharAt(last);
            last-=1;
        }
        return res.toString();
    }
}
// 00 01 02 03
// 10 11 12 13
// 20 21 22 23

// row   = 0
//column = 0


    