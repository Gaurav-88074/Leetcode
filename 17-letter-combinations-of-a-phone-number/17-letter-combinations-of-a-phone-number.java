class Solution {
    private final String[] button = {
        "","","abc","def",
        "ghi","jkl","mno",
        "pqrs","tuv","wxyz"
    };
    private final List<String> result = new ArrayList<>(); 
    public void compute(StringBuilder v,String digits,int pos,int size){
        if(size==digits.length()){
            // System.out.println(v.toString());
            this.result.add(v.toString());
            return;
        }
        int b = digits.charAt(pos) - '0';
        String alphabets = this.button[b];
        for(char c : alphabets.toCharArray()){
            v.append(c);
            compute(v,digits,pos+1,size+1);
            v.deleteCharAt(v.length()-1);
        }
        
    }
    public List<String> letterCombinations(String digits) {
        if(digits.length()==0){
            return this.result;
        }
        StringBuilder v = new StringBuilder();
        compute(v,digits,0,0);
        return this.result;
    }
}