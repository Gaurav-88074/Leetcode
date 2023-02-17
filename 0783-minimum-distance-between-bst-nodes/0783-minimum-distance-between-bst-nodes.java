/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Value{
    public int a;
}
class Solution {
    // public int leftMost(TreeNode root){
    //     if(root.left==null){
    //         return root.val;
    //     }
    //     return leftMost(root.left);
    // }
    public void in(TreeNode root,List<Integer> l,Value value ){
        if(root==null){
            return;
        }
        in(root.left,l,value);
        l.add(root.val);
        if(l.size()>=2){
            value.a = Math.min(value.a ,l.get(l.size()-1) - l.get(l.size()-2));
        }
        in(root.right,l,value);
        
       
    }
    public int minDiffInBST(TreeNode root) {
        List<Integer> l = new ArrayList<>();
        Value value = new Value();
        value.a = Integer.MAX_VALUE;
        in(root,l,value);
       
        return value.a;
        
    }
}