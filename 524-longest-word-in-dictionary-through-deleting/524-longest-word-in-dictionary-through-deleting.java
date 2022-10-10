class Solution {
    public boolean isSubsequence(String s, String t) {
        int p = 0;
        int size = s.length();
        if(size==0){
            return true;
        }
        for(char c : t.toCharArray()){
            if(c==s.charAt(p)){
                p+=1;
            }
            if(p==size){
                return true;
            }
        }
        return false;
    }
    public String findLongestWord(String s, List<String> dictionary) {
        String res = "";
        
        for(String c : dictionary){
            if(isSubsequence(c, s)){
                if(c.length()>res.length()){
                    res = c;
                }
                else if(c.length()==res.length() && c.compareTo(res)<0){
                    res = c;
                }
                
            }
        }
        return res;
    }
}