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
    int res = 0;
    public int go(TreeNode root){
        if(root==null)return 0;
        
        int left = go(root.left);
        int right= go(root.right);
        
        res = Math.max(res, left + 1 + right);
        return 1 + Math.max(left,right);
    }
    public int diameterOfBinaryTree(TreeNode root) {
        if(root==null){
            return  0;
        }
        go(root);
        return res-1;
    }
}