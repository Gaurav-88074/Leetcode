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
            
            return;
        }
        if(dir==1){
            compute(root.left,-1,count+1);
            compute(root.right,1,1);
        }
        else if(dir==-1){
            compute(root.left,-1,1);
            compute(root.right,1,count+1);
        }
        else{
            compute(root.left,-1,1);
            compute(root.right,1,1);
        }
        res = Math.max(res,count);
        
    }
    public int longestZigZag(TreeNode root) {
        // compute(root ,1,0);
        compute(root ,0,0);
        return res;
    }
}