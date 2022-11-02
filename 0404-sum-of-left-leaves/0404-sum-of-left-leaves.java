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
    public void compute(TreeNode root,int which){
        if(root==null){
            return;
        }
        if(root.left==null && root.right==null && which==-2){
            res+=root.val;
        }
        compute(root.left,-2);
        compute(root.right,2);
    }
    public int sumOfLeftLeaves(TreeNode root) {
        compute(root,0);
        return res;
    }
}