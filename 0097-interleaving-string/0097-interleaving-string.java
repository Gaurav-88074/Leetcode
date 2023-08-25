class Solution {
    private Boolean[][][] dp;
    public boolean check(String s1,String s2,String s3,int index,int p1,int p2){
        if( index==s3.length() ) return true;
        
        if( p1==s1.length() && p2==s2.length()) return false;
        //-----------------------------------
        if(dp[index][p1][p2]!=null){
            return dp[index][p1][p2];
        }
        //-----------------------------
        if(p1==s1.length()){
            return (s2.charAt(p2) == s3.charAt(index)) && check(s1,s2,s3,index+1,p1,p2+1);
        }
        if(p2==s2.length()){
            return (s1.charAt(p1) == s3.charAt(index)) && check(s1,s2,s3,index+1,p1+1,p2);
        }
        
        
        boolean case1 =  (s1.charAt(p1) == s3.charAt(index)) && check(s1,s2,s3,index+1,p1+1,p2);

        boolean case2 =  (s2.charAt(p2) == s3.charAt(index)) && check(s1,s2,s3,index+1,p1,p2+1);
        
        dp[index][p1][p2] = case1 || case2;
        return case1 || case2;
        
        
    }
    public boolean isInterleave(String s1, String s2, String s3) {
        if(s1.length()+s2.length() != s3.length()){
            return false;
        }
        dp = new Boolean[s3.length()+1][s1.length()+1][s2.length()+1];
        
        return check(s1,s2,s3,0,0,0);
    }
}