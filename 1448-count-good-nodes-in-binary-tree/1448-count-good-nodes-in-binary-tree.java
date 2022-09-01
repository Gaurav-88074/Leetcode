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
    private int res = 0;
    public void go(TreeNode root,int pathMax){
        if(root==null) return;
        int v = Math.max(root.val,pathMax);
        if(root.val>=pathMax){
            // System.out.println(root.val);
            res+=1;
        }
        go(root.left  ,v);
        go(root.right ,v);
    }
    public int goodNodes(TreeNode root) {
        go(root,-10001);
        return res;
    }
}