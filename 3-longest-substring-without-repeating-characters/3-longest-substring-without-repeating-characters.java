class Solution {
    public int lengthOfLongestSubstring(String s) {
        int[] count = new int[256];
        int low = 0;
        int high=0;
        int chr;
        int res = 0;
        for(int i = 0 ;i < s.length() ; i++){
            chr = s.charAt(i);
            if(count[chr]==0){
                
                high+=1;
                count[chr]+=1;
                res = Math.max(res,high-low);
            }
            else{
                // System.out.println((char)chr+" repeated");
                while(count[chr]>0){
                    count[s.charAt(low)]-=1;
                    low+=1;
                }
                count[chr]+=1;
                
                res = Math.max(res,high-low+1);
                high+=1;
                
            }
        }
        return res;
    
    }
}