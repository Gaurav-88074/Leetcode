/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    public List<List<Integer>> res = new ArrayList<>();
    public void compute(Node root,int level){
        if(root==null){
            return;
        }
        if(res.size()==level){
            res.add(new LinkedList<>());
            res.get(level).add(root.val);
        }
        else{
            res.get(level).add(root.val);
        }
        for(Node child : root.children ){
            compute(child,level+1);
        }
        
    }
    public List<List<Integer>> levelOrder(Node root) {
        compute(root,0);
        return res;
    }
}