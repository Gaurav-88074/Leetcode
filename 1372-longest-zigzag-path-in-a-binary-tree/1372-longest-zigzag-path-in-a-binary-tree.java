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
class Pair{
    int lm;
    int rm;
    public Pair(int a,int b){
        lm = a;
        rm = b;
    }
}
class Solution {
    public int res = 0;
    public void compute(TreeNode root,int dir,int count){
        if(root==null){
            res = Math.max(res,count-1);
            return;
        }
        if(dir==0){
            compute(root.left,1-dir,count+1);
            compute(root.right,1-dir,0);
        }
        else{
            compute(root.left,1-dir,0);
            compute(root.right,1-dir,count+1);
        }
        
    }
    public int longestZigZag(TreeNode root) {
        compute(root ,1,0);
        compute(root ,0,0);
        return res;
    }
}