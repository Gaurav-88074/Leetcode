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
    public boolean check(TreeNode root, int targetSum){
        
        // System.out.println("called");
        if(targetSum==0 && root.left==null && root.right==null){
            return true;
        }
        if(root==null){
            return false;
        }
        
        boolean left = root.left !=null ? check(root.left,targetSum-root.left.val)  : false;
        boolean right= root.right!=null ? check(root.right,targetSum-root.right.val) : false;
        
        return left||right;
    }
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if(root==null){
            return false;
        }
        
        return check(root,targetSum-root.val);
        
    }
}