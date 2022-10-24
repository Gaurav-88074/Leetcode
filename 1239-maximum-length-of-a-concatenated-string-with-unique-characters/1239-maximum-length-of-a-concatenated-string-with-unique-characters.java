class Solution {
    private int[] hash = new int[26];
    // private List<String> array = new ArrayList<>();
    private int res = 0;
    private int count = 0;
    public boolean check(String s){
        int hashIndex;
        boolean ch = true;
        for(char c : s.toCharArray()){
            hashIndex = c-97;
            if (hash[hashIndex]!=0) {
                ch = false;
            }
            hash[hashIndex]+=1;
        }
        for(char c : s.toCharArray()){
            hashIndex = c-97;
            hash[hashIndex]-=1    ;
        }
        return ch;
    }
    public void addInHashTable(String s){
        int hashIndex;
        for(char c : s.toCharArray()){
            hashIndex = c-97;
            hash[hashIndex]+=1; 
        }
    }
    public void removeFromHashTable(String s){
        int hashIndex;
        for(char c : s.toCharArray()){
            hashIndex = c-97;
            hash[hashIndex]-=1; 
        }
    }
    public void concatinateUnique(List<String> strs,int index){
        if (index==strs.size()) {
            // System.out.println(array.toString());
            res = Math.max(res,count);
            return;
        }
        String s = strs.get(index);
        if (check(s)) {
            addInHashTable(s);
            // array.add(s);
            count+=s.length();
            concatinateUnique(strs, index+1);
            count-=s.length();
            // array.remove(array.size()-1);
            removeFromHashTable(s);
        }
        concatinateUnique(strs, index+1);

    }
    public int maxLength(List<String> arr) {
        concatinateUnique(arr, 0);
        return this.res;
    }
}