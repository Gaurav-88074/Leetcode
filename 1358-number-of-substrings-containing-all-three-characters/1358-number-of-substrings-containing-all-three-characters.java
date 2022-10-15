class Solution {
    public boolean check(int[] d){
        return (d[0]>0 && d[1]>0 && d[2]>0);
    }
    public int numberOfSubstrings(String s) {
        int[] d = new int[3];
        int index;
        int res = 0;
        int p= 0;
        for(int i = 0 ; i <s.length() ; i++){
            index = s.charAt(i) - 97;
            d[index]+=1;
            while(check(d)){
                res=res + s.length()-i;
                d[s.charAt(p)-97]-=1;
                p+=1;
            }
        }
        return res;
    }
}