class Solution {
    public String longestPalindrome(String s) {
        
        int res=0;
        
        int low;
        int high;
        
        int size = s.length();
        int pSize;
        
        int start=0;
        int end=0;
        for(int i = 0 ; i<s.length() ; i++){
            //for odd
            low = i;
            high=i+1;
            while(low>-1 && high < size){
                if(s.charAt(low)==s.charAt(high)){
                    
                    pSize = high-low+1;
                    if(pSize>res){
                        res = pSize;
                        start = low;
                        end = high;
                    }
                    
                    low-=1;
                    high+=1;
                }
                else{
                    break;
                }
                
            }
            
            //for even
            low = i-1;
            high=i+1;
            while(low>-1 && high < size){
                if(s.charAt(low)==s.charAt(high)){
                    pSize = high-low+1;
                    if(pSize>res){
                        res = pSize;
                        start = low;
                        end = high;
                    }
                    low-=1;
                    high+=1;
                }
                else{
                    break;
                }
            }
        }
        // System.out.println(start+" - "+end);
        StringBuilder str = new StringBuilder();
        for(int i = start ; i<=end ; i++){
            str.append(s.charAt(i));
        }
        return str.toString();
    }
}