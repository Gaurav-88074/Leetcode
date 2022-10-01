/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
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
        res = count>res ? count : res;
        
    }
    // public int longestZigZag(TreeNode root) {
    //     // compute(root ,1,0);
    
    public int LongestZigZag(TreeNode root) {
        // int res =0;
        compute(root ,0,0);
        return res;
    }
}