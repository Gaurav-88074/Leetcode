class Solution {
    public int minFlips(int a, int b, int c) {
        int res = 0;
        int mask;
        for(int i =0 ; i<32 ; i++){
            mask = (1<<i);
            //checking for set
            if((mask&c)!=0){
//                 if((mask&a)!=0 && (mask&b)!=0){
//                     res+=1;
                    
//                 }
                if((mask&a)==0 && (mask&b)==0){
                    res+=1;
                    // System.out.println("HIT");
                }
            }
            else{
                // System.out.println("At index "+i+" "+(mask&c));
                // System.out.println((mask&a));
                if((mask&a)!=0){
                    res+=1;
                    // System.out.println("HITd");
                }
                if((mask&b)!=0){
                    res+=1;
                    // System.out.println("HITd");
                }
            }
        }
        return res;
    }
}