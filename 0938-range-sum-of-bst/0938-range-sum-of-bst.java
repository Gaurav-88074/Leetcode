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
    public int find(TreeNode root,int low,int high){
        if(root==null){
            return 0;
        }
        if(root.val==low){
            return low;
        }
        else if(low<root.val){
            int v = 0;
            if(root.val<=high &&  root.val>=low){
                v = root.val;
            }
            return v + find(root.left,low,high);
        }
        else{
            int v = 0;
            if(root.val<=high && root.val>=low){
                v = root.val;
            }
            return v + find(root.right,low,high);
        }
        
    }
    public int rangeSumBST(TreeNode root, int low, int high) {
        if(root==null){
            return 0;
        }
        
        int left = rangeSumBST(root.left,low,high); 
        int right = rangeSumBST(root.right,low,high); 
        int v = 0;
        if(root.val<=high&&root.val>=low){
            v += root.val;
        }
        return left+right+v;
        //------------------
        // int left = find(root,low,high); 
        // int right = find(root,low,high); 
        // return left+right-root.val;
    }
}