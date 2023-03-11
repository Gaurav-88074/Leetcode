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
    public int res = 0;
    public void compute(TreeNode root,int value){
        if(root==null){
            return;
        }
        //---------------------------
        value = value<<1;
        value = value | root.val;
        //---------------------------
        if(root.left==null && root.right==null){
            res = res + value;
        }
        //---------------------------
        compute(root.left,value);
        compute(root.right,value);
        //---------------------------
    }
    public int sumRootToLeaf(TreeNode root) {
        compute(root,0);
        return res;
    }
}