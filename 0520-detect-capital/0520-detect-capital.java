class Solution {
    public boolean detectCapitalUse(String word) {
        int c = 0;
        for(int i = 0 ; i<word.length() ; i++){
            if(word.charAt(i) < 97 ){
                c+=1;
            }          
        }
        return c==word.length() || c==0 ||(c==1 && word.charAt(0)<97);
    }
}