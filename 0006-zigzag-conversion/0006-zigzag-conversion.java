class Solution {
    public String convert(String s, int numRows) {
        if(numRows==1){
            return s;
        }
        int col = 500;
        int[][] m = new int[numRows][col];
        StringBuilder res = new StringBuilder();
        int i = 0;
        int j = 0;
        int activatedMode = 0;
        
        for(char c : s.toCharArray()){
            if(activatedMode == 0){
                m[i][j] = c;
                i+=1;
            }
            else{
                j+=1;
                i-=1;
                m[i][j] = c;
                // j+=1;
            }
            if(i!=0 && i%numRows==0){
                activatedMode = 1;   
                i-=1;
            }
            if(i==0){
                activatedMode = 0;   
                i+=1;
            }
        }
        // for(int k = 0 ; k< numRows ; k++){
        //     System.out.println(Arrays.toString(m[k]));
        // }
        for(int p = 0 ;p<numRows ; p++){
            for(int q = 0 ;q<col ; q++){
                if(m[p][q]!=0){
                    res.append((char)m[p][q]);
                }
            }
        }
        return res.toString();
    }
}