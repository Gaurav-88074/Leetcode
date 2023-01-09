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
    public List<Integer> res = new LinkedList<>();
    public List<Integer> preorderTraversal(TreeNode root) {
        TreeNode current = root; 
        TreeNode iPre = null; 
        while(current!=null){
            if(current.left!=null){
                iPre = current.left;
                while(iPre.right!=null){
                    iPre=iPre.right;
                }
                iPre.right = current.right;
                current.right = current.left;
                res.add(current.val);
                current = current.right;
            }
            else{
                res.add(current.val);
                current = current.right;
            }
        }
        return res;
    }
}