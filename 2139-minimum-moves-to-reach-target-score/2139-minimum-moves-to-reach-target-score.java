class Solution {
    public int minMoves(int target, int d) {
        int res = 0;
        int given = target;
        while (given!=1){
            if ((given&1)==0 && d>0){
                given/=2;
                d-=1;
            }
            else{
                given-=1;
            }
            if (d==0){
                return res+given;
            }
            res+=1;
        }
        return res;
    }
}