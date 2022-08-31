class Solution {
    public int maxScoreSightseeingPair(int[] values) {
        int p1 = 0;
        
        int lmax = 0;
        int res = 0;
        
        for(int i=1 ; i<values.length ; i++){
            
            res = Math.max(res ,values[p1] + values[i] + (p1 - i) );
            // System.out.println(res);
            
            if(i + values[i] >values[p1] + p1 ){
                p1= i;
            }
        }
        return res;
    }
}