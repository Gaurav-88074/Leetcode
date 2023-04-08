/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution{
    HashMap<Integer,Node> map = new HashMap<>();
    public Node copy(Node original){
       
        Node res = new Node();
        res.val = original.val;
        
        //----------------
        map.put(res.val,res);
        //----------------
        
        for(Node child : original.neighbors){
            if(!map.containsKey(child.val)){
                res.neighbors.add(copy(child));
            }
            else{
                res.neighbors.add(map.get(child.val));
            }
        }
        
        return res;
    }
    public Node cloneGraph(Node node) {
        if(node==null) return null;
        return copy(node);
    }
}