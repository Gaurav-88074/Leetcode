class node{
    public node[] next ;
    public boolean isEnd = false;
    public node(){
        this.next = new node[76];
    }
}
class Trie {
    private node root = null;
    public Trie() {
        this.root = new node();
    }
    public boolean insert(node root,String word,int index) {
        if(index==word.length()){
            root.isEnd = true;
            return true;
        }
        int ch = word.charAt(index)-47;
        if( root.isEnd==true && word.charAt(index)=='/'){
            return false;
        }
        if(root.next[ch]==null) root.next[ch] = new node();
        
        return insert(root.next[ch],word,index+1);
    }
    public boolean insert(String word) {
        return insert(root,word,0);
    }
}

class Solution {
    public List<String> removeSubfolders(String[] folder) {
        Arrays.sort(folder);
        var trie = new Trie();
        List<String> res = new ArrayList<>();
        for(String s : folder){
            if(trie.insert(s)){
                res.add(s);
            }
        }
        return res;
    }
}