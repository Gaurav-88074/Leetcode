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
    public int val;
    public boolean compute(TreeNode root){
        if(root==null)return true;
        return root.val==val && compute(root.left) && compute(root.right);
    }
    public boolean isUnivalTree(TreeNode root) {
        if(root==null)return true;
        val = root.val;
        return compute(root);
        
    }
}