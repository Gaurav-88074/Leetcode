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
    public int getHeight(TreeNode root){
        if(root==null){
            return -1;
        }
        return 1 + getHeight(root.left);
    }
    public int countNodes(TreeNode root) {
        int h = getHeight(root);
        
        return h<0 ? 0 : 
                    h-1==getHeight(root.right) ? (1<<h) +  countNodes(root.right) : 
                        (1<<h-1) + countNodes(root.left);
    }
}