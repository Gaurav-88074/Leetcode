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
class Solution {
    public TreeNode res = new TreeNode(0);
    public TreeNode temp= res;
    public void compute(TreeNode root){
        if(root==null){
            return;
        }
        compute(root.left);
        
        //--------------------
        root.left = null;
        temp.right = root;
        temp.left = null;
        temp=temp.right;
        //--------------------
        
        compute(root.right);
    }
    public TreeNode increasingBST(TreeNode root) {
        compute(root);
        return res.right;
    }
}