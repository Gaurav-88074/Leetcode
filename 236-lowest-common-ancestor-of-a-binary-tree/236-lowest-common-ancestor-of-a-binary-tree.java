/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean isPresent(TreeNode root,int value){
        if(root==null) return false;
        
        else if(root.val==value) return true;
        
        boolean left =  isPresent(root.left,value);
        
        boolean right= isPresent(root.right,value);
        
        return left || right;
            
    }
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root==null){
            return root;
        }
        TreeNode left  = lowestCommonAncestor(root.left ,p,q);
        TreeNode right = lowestCommonAncestor(root.right,p,q);
        //--------------------------
        if(left!=null){
            return left;
        }
        //---------------------------
        if(right!=null){
            return right;
        }
        //---------------------------
        if(isPresent(root,p.val) && isPresent(root,q.val)){
            return root;
        }
        
        return null;
    }
}