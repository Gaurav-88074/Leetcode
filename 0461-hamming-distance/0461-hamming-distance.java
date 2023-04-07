class Solution {
    public int hammingDistance(int x, int y) {
        int res = 0;
        int mask = 1;
        while(x>0 && y>0){
            if( 
                ((mask&x)==1 && (mask&y)==0)
                ||
                ((mask&x)==0 && (mask&y)==1)
                
                ){
                res+=1;
            }
            x>>=1;
            y>>=1;
        }
        while(x>0){
            if((mask&x)==1){
                res+=1;
            }
            x>>=1;
        }
        while(y>0){
            if((mask&y)==1){
                res+=1;
            }
            y>>=1;
        }
        return res;
    }
}