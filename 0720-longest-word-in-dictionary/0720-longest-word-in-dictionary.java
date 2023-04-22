class node{
    public node[] next ;
    public boolean isEnd = false;
    // public boolean isEligible = true;
    public node(){
        this.next = new node[26];
    }
}
class Trie {
    private node root = null;
    public Trie() {
        this.root = new node();
    }
    public String res ="";
    // public StringBuilder temp = new StringBuilder();
    public void insert(node root,String word,int index,boolean isE,int visit) {
        if(index==word.length()){
            root.isEnd = true;
            if(visit==1 || isE==true){
                if(res.length()==word.length()){
                    if(res.compareTo(word)>0){
                        res = word;
                    }
                }
                else if(word.length()> res.length()){
                    res = word;
                }
            }
            else{
                // System.out.println("happend while adding "+word);
                // root.isEligible = false;
            }
            return;
        }
        int ch = word.charAt(index)-97;
        
        if(visit>=1){
            isE = isE  && root.isEnd; 
        }
        if(root.next[ch]==null){
            root.next[ch] = new node();
            
        }
        
            
        insert(root.next[ch],word,index+1,isE,visit+1);
    }
    public void insert(String word) {
        boolean isE = true;
        int visit =0;
        insert(root,word,0, isE,visit);
    }
}

class Solution {
    public String longestWord(String[] words) {
        Arrays.sort(words);
        
        Trie trie = new Trie();
        for(String s : words){
            // System.out.println(s);
            trie.insert(s);
        }
        return trie.res;
    }
}