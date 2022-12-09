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
    public void go(TreeNode root,int minValue,int maxValue){
        if(root==null) return;
        
        go(root.left,Math.min(root.val,minValue),Math.max(root.val,maxValue));
        
        res = res>Math.abs(root.val-minValue) ? res : Math.abs(root.val-minValue);
        res = res>Math.abs(root.val-maxValue) ? res : Math.abs(root.val-maxValue);
        
        go(root.right,Math.min(root.val,minValue),Math.max(root.val,maxValue));
    }
    public int maxAncestorDiff(TreeNode root) {
        go(root,root.val,root.val);
        return res;
    }
}