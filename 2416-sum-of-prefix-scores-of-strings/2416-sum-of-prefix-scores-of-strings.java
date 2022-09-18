class node{
    public node[] next ;
    public boolean isEnd = false;
    public int count = 0; 
    public node(){
        this.next = new node[26];
    }
}

class Solution {
    public int[] sumPrefixScores(String[] words) {
        int[] res = new int[words.length];
        Trie obj = new Trie();
        for(String s : words){
            obj.insert(s);
        }
        for(int i =0 ; i< words.length ; i++){
            
            res[i] = obj.getAns(words[i]);
        }
        
        return res;
        
    }
}
class Trie {
    public node root = null;
    public Trie() {
        this.root = new node();
    }
    public int getAns(node root,String word,int index){
        if(index==word.length()){
            
            return 0 ;
        }
        int ch = word.charAt(index)-97;
        if(root.next[ch]==null){
            return 0;
        }
        node upNext = root.next[ch];
        
        return upNext.count + getAns(root.next[ch],word,index+1);
    }
    public int getAns(String word){
        return getAns(root,word,0);
    }
    public void insert(node root,String word,int index) {
        
        if(index==word.length()){
            // root.isEnd = true;
            return;
        }
        
        int ch = word.charAt(index)-97;
        if(root.next[ch]==null) root.next[ch] = new node();
        node upNext = root.next[ch];
        upNext.count+=1;
        insert(upNext,word,index+1);
    }
    public void insert(String word) {
        insert(root,word,0);
    }
    public boolean search(node root,String word,int index) {
        if(index==word.length()){
            return root.isEnd;
        }
        int ch = word.charAt(index)-97;
        if(root.next[ch]==null){
            return false;
        }
        return search(root.next[ch],word,index+1);
    }
    public boolean search(String word) {
        return search(root,word,0);
    }
    public boolean startsWith(node root,String prefix,int index) {
        if(prefix.length() == 0){
            return true;
        }
        if(index==prefix.length()){
            return true;
        }
        int ch = prefix.charAt(index)-97;
        if(root.next[ch]==null){
            return false;
        }
        return startsWith(root.next[ch],prefix,index+1);
    }
    public boolean startsWith(String prefix) {
        return startsWith(root,prefix,0);
    }
}

