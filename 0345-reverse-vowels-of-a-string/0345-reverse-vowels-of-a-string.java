class Solution {
    private Set<Character> set = new HashSet<>();
    private Queue<Character> queue = new LinkedList<>();
    public void reverse(char[] s,int index){
        if(index==s.length){
            return;
        }
        if(set.contains(s[index])){
            queue.add(s[index]);
        }
        reverse(s,index+1);
        if(set.contains(s[index])){
            s[index] = queue.poll();
        }
        
    }
    public String reverseVowels(String s) {
        // StringBuilder res = new StringBuilder(s);
        char[] res = s.toCharArray();
        set.add('a');
        set.add('e');
        set.add('i');
        set.add('o');
        set.add('u');
        set.add('A');
        set.add('E');
        set.add('I');
        set.add('O');
        set.add('U');
        
        reverse(res,0);
        
        return new String(res);
    }
}