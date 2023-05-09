class node{
    public node[] next ;
    public boolean isEnd = false;
    public node(){
        this.next = new node[26];
    }
}
class Trie {
    private node root = null;
    private StringBuilder ts ;
    private int count;
    private List<String> tl ;
    public Trie() {
        this.root = new node();
    }
    
    public void insert(node root,String word,int index) {
        if(index==word.length()){
            root.isEnd = true;
            return;
        }
        int ch = word.charAt(index)-97;
        if(root.next[ch]==null) root.next[ch] = new node();
        insert(root.next[ch],word,index+1);
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
    public void getStartsWith(String prefix,node root,int index){
        // if(count>=3){
            // System.out.println(ts);
            // return;
        // }
        if(prefix.length() == 0 || index>=prefix.length()){
            node obj=null;
            for(int i = 0 ; i<26 ; i++){
                obj = root.next[i];
                if(obj!=null){
                    ts.append((char)(i+97));
                    getStartsWith(prefix,obj,index+1);
                    ts.deleteCharAt(ts.length()-1);
                }
            }
            if(root.isEnd==true){
                // System.out.println(ts);
                tl.add(ts.toString());
                count+=1;
            }
            return;
        }
        int ch = prefix.charAt(index)-97;
        if(root.next[ch]==null){
            return;
        }
        ts.append( prefix.charAt(index));//prefix chars
        getStartsWith(prefix,root.next[ch],index+1);
    }
    public List<String> getStartsWith(String prefix){
        ts= new StringBuilder();
        count = 0;
        
        tl = new ArrayList<>();
        
        getStartsWith(prefix,root,0);
        Collections.sort(tl);
        if(tl.size()>3){
            return tl.subList(0, 3);
        }
        return tl;
        
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
class Solution {
    public List<List<String>> suggestedProducts(String[] products, String searchWord) {
        Trie trie= new Trie();
        // Arrays.sort(products);
        for(String s : products){
            trie.insert(s);
        }
        List<List<String>> res = new LinkedList<>();
        for(int i =0 ; i<searchWord.length() ; i++){
            List<String> ee = trie.getStartsWith(searchWord.substring(0,i+1));
            res.add(ee);
            // System.out.println("====");
        }
        
        return res;
    }
}