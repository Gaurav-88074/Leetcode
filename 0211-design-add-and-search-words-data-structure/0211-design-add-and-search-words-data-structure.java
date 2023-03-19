class node{
    public node[] next ;
    public boolean isEnd = false;
    public node(){
        this.next = new node[26];
    }
}
class WordDictionary {
    private node root = null;
    //---------------------------------------------------
    public WordDictionary() {
        this.root = new node();
    }
    //-----------------------------------------------------
    public void insert(node root,String word,int index) {
        if(index==word.length()){
            root.isEnd = true;
            return;
        }
        int ch = word.charAt(index)-97;
        if(root.next[ch]==null) root.next[ch] = new node();
        insert(root.next[ch],word,index+1);
    }
    //-----------------------------------------------------
    public void addWord(String word) {
        insert(root,word,0);
    }
    //-------------------------------------------------------
    public boolean search(node root,String word,int index) {
        if(index==word.length()){
            return root.isEnd;
        }
        int ch = word.charAt(index)-97;
        //--------------------------------
        if(ch==-51){
            boolean res = false;
            for(int i = 0 ;i< 26 ;i++ ){
                if(root.next[i]!=null)
                    res = res ||  search(root.next[i],word,index+1);
            }
            return res;
        }
        //---------------------------------
        if(root.next[ch]==null){
            return false;
        }
        return search(root.next[ch],word,index+1);
    }
    //---------------------------------------------------------
    public boolean search(String word) {
        return search(root,word,0);
    }
    //----------------------------------------------------------
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */