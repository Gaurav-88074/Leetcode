class Solution {
    public int countSubstrings(String s) {
        int left = 0;
        int right= 0;
        int res  = 0;
        for(int i = 0; i <s.length() ; i++){
            //for odd strings
            left  = i;
            right = i;
            while(left>=0 && right<s.length() && s.charAt(left)==s.charAt(right)){
                res+=1;
                left-=1;
                right+=1;
            }
            
            //for even strings
            left  = i;
            right = i+1;
            while(left>=0 && right<s.length() && s.charAt(left)==s.charAt(right)){
                res  +=1;
                left -=1;
                right+=1;

            }
        }
        return res;
    }
}