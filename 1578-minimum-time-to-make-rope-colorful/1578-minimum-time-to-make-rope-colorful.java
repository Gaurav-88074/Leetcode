class Solution {
    public int minCost(String colors, int[] neededTime) {
        int c = 0;
        int totalSum = 0;
        int m = 0;
        
        char pre = colors.charAt(0);
        c =1;
        m = neededTime[0];

        int i;
        for(i =1; i <colors.length() ; i++){
            
            if(colors.charAt(i)==pre){
                c+=1;
                m = Math.max(m,neededTime[i]);
                totalSum+=neededTime[i-1];
            }
            else{
                if(c>1){
                    totalSum+=neededTime[i-1];
                    totalSum-= m;
                    // System.out.println("At index :"+i+" "+m);
                }
                c=1;
                pre = colors.charAt(i);
                m = neededTime[i];
            }
            
        }
        if(c>1){
            totalSum+=neededTime[i-1];
            totalSum-= m;
            // System.out.println("At index :"+i+" "+m);         
        }
        return totalSum;
    }
}